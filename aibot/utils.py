def format_data(data):
    # Function to format data for output
    return str(data)

def log_message(message):
    # Function to log messages to a file or console
    print(f"LOG: {message}")

def validate_input(input_data):
    # Function to validate user input
    if not input_data:
        raise ValueError("Input data cannot be empty.")
    return True

def parse_response(response):
    # Function to parse the response from the AI agent
    return response.get('choices', [{}])[0].get('text', '').strip()