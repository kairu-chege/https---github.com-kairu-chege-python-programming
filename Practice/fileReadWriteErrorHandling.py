import os # this module provides functions for interacting with the operating system

"""this function modifies the contents of an input file and writes the modified
content to an output file """
def modify_file(input_file, output_file):
    
    try:
        #The with statement ensures that the files are closed properly, even if exceptions occur.
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
              #modify the line here(capitalizes each word)
              modified_line = ' '.join(word.capitalize() for word in line.split())
              #writes the modified line to the output file
              f_out.write(modified_line)
    #handling of potential filenotfouderror and ioerror exceptions
    except FileNotFoundError:
        print(f"Error: Input file {input_file}' not found")
    except IOError as e:
        print(f"Error: I/O error occured: {e} !")
        
if __name__ == "__main__":
    #prompting the user for the input and output file names
    input_filename = input("Enter the name of your input file: ")
    output_filename = input("Enter the name of your output file: ")
    
    #the function takes an input file, modifies its content, and creates a new output file with the modified content.
    modify_file(input_filename, output_filename)