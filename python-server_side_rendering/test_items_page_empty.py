import requests

def test_items_page_empty():
    base_url = 'http://127.0.0.1:5000'
    
    # Realiza una solicitud GET a la ruta /items
    response = requests.get(f'{base_url}/items')
    
    # Verifica que el código de estado de la respuesta sea 200
    assert response.status_code == 200, "Failed: Items page did not return status code 200"
    
    # Verifica que el contenido HTML contenga "No items found" si la lista está vacía
    assert "No items found" in response.text, "Failed: 'No items found' message not displayed"

if __name__ == '__main__':
    test_items_page_empty()
