import os

def fix_file():
    with open('index.html', 'rb') as f:
        content = f.read().decode('utf-8')
    
    # Fix conflict markers
    content = content.replace('<<<<<<< HEAD\r\n</html>\r\n=======\r\n</html>\r\n>>>>>>> fbded9d (.)\r\n', '</html>\r\n')
    content = content.replace('<<<<<<< HEAD\n</html>\n=======\n</html>\n>>>>>>> fbded9d (.)\n', '</html>\n')
    
    # Fix the last line in case it doesn't have a trailing newline
    content = content.replace('<<<<<<< HEAD\n</html>\n=======\n</html>\n>>>>>>> fbded9d (.)', '</html>')
    content = content.replace('<<<<<<< HEAD\r\n</html>\r\n=======\r\n</html>\r\n>>>>>>> fbded9d (.)', '</html>')
    
    # Fix email links
    content = content.replace(
        'href="mailto:saitanmai6969@gmail.com"',
        'href="https://mail.google.com/mail/?view=cm&fs=1&to=saitanmai6969@gmail.com" target="_blank"'
    )
    
    # Add rel="noopener noreferrer" just after target="_blank"
    # Actually wait, the replacement string is easier if I combine it.
    
    with open('index.html', 'wb') as f:
        f.write(content.encode('utf-8'))

if __name__ == '__main__':
    fix_file()
