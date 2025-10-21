import secrets
import webbrowser
import requests
import os
import sys
from urllib.parse import urlencode, urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

# ============================================================================
# CONFIGURATION - Chargée depuis config.yaml
# ============================================================================

try:
    from config_loader import load_config

    config = load_config()
    linkedin_config = config.get_linkedin_config()

    CLIENT_ID = linkedin_config['oauth']['client_id']
    CLIENT_SECRET = linkedin_config['oauth']['client_secret']

    # Redirect URI depuis config ou valeur par défaut
    REDIRECT_URI = linkedin_config['oauth'].get('redirect_uri', 'https://www.linkedin.com/developers/tools/oauth/redirect')

    # Scopes depuis la config ou valeurs par défaut
    SCOPES = " ".join(linkedin_config['oauth'].get('scopes', [
        "r_ads",
        "rw_ads",
        "r_ads_reporting",
        "r_ads_leadgen_automation",
        "r_basicprofile",
        "r_liteprofile",
        "r_organization_social",
        "r_organization_admin",
        "w_organization_social",
        "rw_organization_admin",
        "w_member_social",
        "r_1st_connections_size",
        "r_marketing_leadgen_automation",
        "r_events",
        "rw_events"
    ]))

except (ImportError, FileNotFoundError, KeyError) as e:
    print(f"\n⚠️  ERREUR: Impossible de charger la configuration depuis config.yaml")
    print(f"   Détails: {e}")
    print("\n   Veuillez créer config.yaml depuis config.example.yaml")
    print("   et remplir les informations LinkedIn OAuth\n")
    sys.exit(1)

# ============================================================================


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Handler pour récupérer le code OAuth depuis le callback"""
    
    authorization_code = None
    state_received = None
    
    def do_GET(self):
        # Parser l'URL
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        # Extraire le code et le state
        if 'code' in params:
            OAuthCallbackHandler.authorization_code = params['code'][0]
            OAuthCallbackHandler.state_received = params.get('state', [None])[0]
            
            # Réponse HTML
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
            <html>
            <head><title>LinkedIn OAuth</title></head>
            <body style="font-family: Arial; padding: 50px; text-align: center;">
                <h1 style="color: #0077B5;">✓ Autorisation réussie!</h1>
                <p>Vous pouvez fermer cette fenêtre et retourner au terminal.</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
            
        elif 'error' in params:
            error = params['error'][0]
            error_desc = params.get('error_description', [''])[0]
            
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = f"""
            <html>
            <head><title>Erreur OAuth</title></head>
            <body style="font-family: Arial; padding: 50px; text-align: center;">
                <h1 style="color: #DC143C;">✗ Erreur d'autorisation</h1>
                <p><strong>Erreur:</strong> {error}</p>
                <p>{error_desc}</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        # Désactiver les logs du serveur HTTP
        pass


def get_access_token_manual():
    """Méthode manuelle pour les URIs non-localhost"""
    
    # Générer un state sécurisé
    state = secrets.token_urlsafe(32)
    
    print("=" * 70)
    print("GÉNÉRATION DU TOKEN LINKEDIN - MÉTHODE MANUELLE")
    print("=" * 70)
    print(f"\n1. State de sécurité généré: {state}")
    print("   (Gardez cette valeur pour vérification)")
    
    # Construire l'URL d'autorisation
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'state': state,
        'scope': SCOPES
    }
    
    auth_url = f"https://www.linkedin.com/oauth/v2/authorization?{urlencode(params)}"
    
    print("\n2. Ouverture de la page d'autorisation LinkedIn...")
    print(f"   URL: {auth_url}\n")
    
    # Ouvrir le navigateur
    webbrowser.open(auth_url)
    
    print("3. Autorisez l'application dans votre navigateur")
    print("4. Vous serez redirigé vers une page avec un code")
    
    # Si on utilise l'outil LinkedIn officiel
    if "linkedin.com/developers/tools" in REDIRECT_URI:
        print("\n   Sur la page de redirection LinkedIn:")
        print("   - Copiez le 'code' affiché")
        print("   - Copiez le 'state' affiché")
    else:
        print(f"\n   Sur la page de redirection ({REDIRECT_URI}):")
        print("   - Copiez le paramètre 'code' de l'URL")
        print("   - Copiez le paramètre 'state' de l'URL")
    
    # Demander le code
    print("\n" + "-" * 70)
    code = input("Entrez le CODE reçu: ").strip()
    received_state = input("Entrez le STATE reçu: ").strip()
    
    # Vérifier le state
    if received_state != state:
        print("\n✗ ERREUR: Le state ne correspond pas!")
        print(f"  Attendu: {state}")
        print(f"  Reçu: {received_state}")
        return None
    
    print("\n✓ State vérifié avec succès")
    
    # Échanger le code contre un access token
    return exchange_code_for_token(code)


def get_access_token_localhost():
    """Méthode automatique avec serveur local"""
    
    # Extraire le port de la REDIRECT_URI
    parsed = urlparse(REDIRECT_URI)
    port = parsed.port or (443 if parsed.scheme == 'https' else 80)
    
    # Générer un state sécurisé
    state = secrets.token_urlsafe(32)
    
    print("=" * 70)
    print("GÉNÉRATION DU TOKEN LINKEDIN - MÉTHODE AUTOMATIQUE")
    print("=" * 70)
    print(f"\n1. Démarrage du serveur local sur le port {port}...")
    
    # Construire l'URL d'autorisation
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'state': state,
        'scope': SCOPES
    }
    
    auth_url = f"https://www.linkedin.com/oauth/v2/authorization?{urlencode(params)}"
    
    print("\n2. Ouverture de la page d'autorisation LinkedIn...")
    webbrowser.open(auth_url)
    
    print("\n3. En attente de l'autorisation...")
    print("   Autorisez l'application dans votre navigateur")
    
    # Démarrer le serveur pour récupérer le callback
    try:
        server = HTTPServer(('localhost', port), OAuthCallbackHandler)
        server.handle_request()
        
        # Récupérer les valeurs
        code = OAuthCallbackHandler.authorization_code
        received_state = OAuthCallbackHandler.state_received
        
        if not code:
            print("\n✗ Aucun code d'autorisation reçu")
            return None
        
        # Vérifier le state
        if received_state != state:
            print("\n✗ ERREUR: Le state ne correspond pas!")
            return None
        
        print("\n✓ Code d'autorisation reçu avec succès")
        
        # Échanger le code contre un token
        return exchange_code_for_token(code)
        
    except Exception as e:
        print(f"\n✗ Erreur lors du démarrage du serveur: {e}")
        print("Utilisez la méthode manuelle à la place")
        return None


def exchange_code_for_token(code):
    """Échange le code d'autorisation contre un access token"""
    
    print("\n4. Échange du code contre un access token...")
    
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    
    response = requests.post(
        'https://www.linkedin.com/oauth/v2/accessToken',
        data=token_data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    
    if response.status_code == 200:
        token_info = response.json()
        
        print("\n" + "=" * 70)
        print("✓ ACCESS TOKEN GÉNÉRÉ AVEC SUCCÈS!")
        print("=" * 70)
        print(f"\nAccess Token:\n{token_info['access_token']}\n")
        print(f"Type: {token_info.get('token_type', 'Bearer')}")
        print(f"Expire dans: {token_info.get('expires_in', 'N/A')} secondes")
        
        if 'refresh_token' in token_info:
            print(f"\nRefresh Token:\n{token_info['refresh_token']}")
        
        print("\n" + "=" * 70)
        print("Copiez l'Access Token ci-dessus pour l'utiliser dans votre pipeline")
        print("=" * 70)
        
        return token_info
        
    else:
        print("\n✗ ERREUR lors de l'obtention du token")
        print(f"Status: {response.status_code}")
        print(f"Réponse: {response.text}")
        return None


def main():
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "GÉNÉRATEUR DE TOKEN LINKEDIN OAUTH" + " " * 19 + "║")
    print("╚" + "═" * 68 + "╝")
    
    # Vérifier la configuration
    if CLIENT_ID == "votre_client_id_ici":
        print("\n⚠️  ATTENTION: Vous devez configurer CLIENT_ID et CLIENT_SECRET")
        print("   Éditez le script et remplacez les valeurs en haut du fichier\n")
        return
    
    print(f"\nConfiguration:")
    print(f"  Client ID: {CLIENT_ID[:20]}...")
    print(f"  Redirect URI: {REDIRECT_URI}")
    print(f"  Scopes: {SCOPES}")
    
    # Choisir la méthode selon l'URI
    if "localhost" in REDIRECT_URI:
        print("\n→ Méthode: Automatique (serveur local)")
        get_access_token_localhost()
    else:
        print("\n→ Méthode: Manuelle (copier-coller)")
        get_access_token_manual()


if __name__ == "__main__":
    main()