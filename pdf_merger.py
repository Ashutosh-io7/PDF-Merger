import os 
from pypdf import PdfWriter

def merge_pdfs (input_files , output_filename = 'merged_file.pdf') : 
    """
    Merges a list of PDF files into a single PDF
    """

    merger = PdfWriter() 

    print('Starting PDF merge process..') 
    try : 
        for pdf in input_files : 
            if not os.path.exists(pdf) : 
                print(f"Error : The file {pdf} does not exist.")
                return 

            print(f"Adding : {pdf}")
            merger.append(pdf) 

        merger.write(output_filename)
        print(f"Success !! Created {output_filename}") 

    except Exception as e : 
        print(f"Error Occurred : {e}") 

    finally : 
        merger.close() 

if __name__ == "__main__" : 

    print('Welcome to PDF Merger !!')
    print('----------------------------------------')
    
    files_to_merge = [] 

    n = int(input('How many pdfs do you want to merge ? : ')) 

    if n >= 2 : 
        for i in range(1 , n+1) : 
            name = input(f"Enter the Name of PDF {i} : ").strip() 
            files_to_merge.append(name)
            
        merge_pdfs(files_to_merge)
    else : 
        print('Please Enter a Valid Choice') 