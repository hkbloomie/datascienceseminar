#having a function that isolates the comments
import sys



# format of copy and paste of comments

# 1w3,169 likesReply
# centenno_'s profile picture
# The crossover I didn't expect

# turn txt file into a list of lines



def comment_isolator(infile, outfile):
    #turn file into a list? 
    # Write the comments to the output file
    for _ in range(2):
            infile.readline()
    
    for line in infile:
        for _ in range(2):
            infile.readline()
        # if not line.strip():  # Skip empty lines
        #     continue
        # if line.strip().isdigit():  # Skip numeric lines like "169 likes"
        #     continue
        outfile.write(line.strip() + '\n') 
    

#having a function that isolates the emojis based on ASCII value 

def emoji_isolator():
    return



if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # lines = infile.readlines()
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            comment_isolator(infile, outfile)
            print("Comments isolated successfully.")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", e)
