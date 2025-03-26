# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# File Name : main.py
# Student Name: Luke Elmore, Vanshika Rana
# email:  elmorels@mail.uc.edu, ranava@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   03/27/2025 
# Course #/Section:   IS 4010-002
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment is a group project under which we had to fork a given Python repo, add a team image and create data visualization, then submit via GitHub.
# Brief Description of what this module does: This module is about exploring AI benchmark data and learning how to process and structure it using Python tools and CSV files.
# Citations: We used ChatGPT AI Model. 
# Anything else that's relevant: N/A


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.image as img
from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *
from GraphicPackage.Graphic import *
if __name__ == "__main__":
  
    img1 = mpimg.imread("image/aim_powerpc601.jpg")
    img2 = mpimg.imread("image/2070_super.jpg")

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(img1)
    axes[0].axis('off')
    axes[0].set_title("Team: AIM PowerPC 601")

    axes[1].imshow(img2)
    axes[1].axis('off')
    axes[1].set_title("2070 Super")

    plt.tight_layout()
    plt.show()

    plot_readability_chart()


    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")

 
    myPDF = PDFUtilities()
    myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    print("The first question:")
    print(questions[0])
    
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #print("\ntext from dictionaries:", text[0:500])

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
    
    
    #1. Perform reading level analysis on the big string and print the results to the console.
    Reading_Level.compute_readability_indices("MMLU", text)

    #2. Process the big string to find the longest word


    #3. Process the big string to find the most prevalent word
    

    #4. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file
    

    #5. Perform some data visualization on the text. Research Data Vis libraries and apply one.
     

    #6a. Write all the questions and possible answers (without the correct answer) to a text file. Use a CSV format and create a unique identifier field for each question.
    #6b. Write the question identifier (see 6a, above) and the correct answer to another text file. Use a CSV format.
    questions_written = write_questions_to_text_files("MMLU", questions)
    print(questions_written, "questions written to the file.")
    
    """
    # This code is commented out
    #Reading_Level.test01()

    text = "This is a sentence that we can use to test the reading level computations. "
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
            
    # A test with text at a higher reading level
    text = "Birds, employing a combination of aerodynamic principles and specialized anatomical adaptations, achieve flight through the generation of lift, which counteracts the force of gravity."
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
    """
