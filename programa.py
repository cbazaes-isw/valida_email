# pylint: disable=C0103
"""
Valida los siguiente:
- formato
- dns
- casilla
"""
import util

def lambda_handler(event, context):
    """
    Valida los siguiente:
    - formato
    - dns
    - casilla
    """
    email = event["email"]

    esValido = util.emailValido(email)
    return esValido
