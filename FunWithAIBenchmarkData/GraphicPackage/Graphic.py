# File Name :  Graphic.py
# Student Name: Luke Elmore, Vanshika Rana
# email:  elmorels@mail.uc.edu, ranava@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   03/27/2025 
# Course #/Section:   IS 4010-002
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment is a group project under which we had to fork a given Python repo, add a team image and create data visualization, then submit via GitHub.
# Brief Description of what this module does: This module does takes the reading levels with the different stages in life
# Citations: We used ChatGPT AI Model. 
# Anything else that's relevant: N/A

import matplotlib.pyplot as plt

def plot_readability_chart():
    # Define the readability indices and their average values for different reading levels
    reading_levels = ["Grade 12", "College", "Undergraduate", "High School", "Middle School", "Elementary"]
    flesch_kincaid_grade = [12, 14, 16, 10, 8, 5]  # Approximate values for each level
    gunning_fog = [15, 14, 13, 12, 10, 8]  # Approximate values for each level
    coleman_liau = [12, 14, 15, 10, 8, 6]  # Approximate values for each level
    ari = [12, 14, 16, 10, 8, 5]  # Approximate values for each level

    # Plot the chart
    plt.figure(figsize=(10, 6))
    plt.plot(reading_levels, flesch_kincaid_grade, label="Flesch-Kincaid Grade", marker='o')
    plt.plot(reading_levels, gunning_fog, label="Gunning Fog Index", marker='o')
    plt.plot(reading_levels, coleman_liau, label="Coleman-Liau Index", marker='o')
    plt.plot(reading_levels, ari, label="Automated Readability Index (ARI)", marker='o')

    # Adding labels and title
    plt.xlabel("Reading Level")
    plt.ylabel("Readability Score")
    plt.title("Readability Indices vs Reading Levels")
    plt.legend()

    # Show the chart
    plt.grid(True)
    plt.tight_layout()
    plt.show()
