def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name.""" # <--- DOCSTRING
    
    # Check if inputs are empty strings # <--- COMMENT (#)
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
        
    return f"{f_name.title()} {l_name.title()}"