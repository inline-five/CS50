#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return 1;
    }
    
    //create pointer to card file if valid
    FILE *card = fopen(argv[1], "r"); 
    
    if (card == NULL)
    {
        return 1;
    }
    
    //intialize variables
    int counter = 0; //counter for each image
    char filename[8]; //array for image name
    BYTE buffer[512]; //array for each 512 bit section of file
    FILE *img; // intilizaing a pointer to img of type FILE
    int is_open = 0; // bool switch if file is open or not (0 is closed, 1 is open)
    
    // card == card.raw recovery file (provided)
    // img == new file for image 
    // filename == img file name


    //begin read cycle
    while (fread(buffer, 512, 1, card) == 1) //start reading the file
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) 
        {
            if (counter > 0) // if new image detected outside of first run, closes old img out
            {
                fclose(img);
            }
            
            sprintf(filename, "%03i.jpg", counter); // create file name
            img = fopen(filename, "w"); // open up a new file to write to
            is_open = 1; // bool switch for if new file is open or not
            counter++; // keeps track of counter for img name
            fwrite(buffer, 512, 1, img);
        }
        
        else if (buffer[0] != 0xff || buffer[1] != 0xd8 || buffer[2] != 0xff || (buffer[3] & 0xf0) != 0xe0)     
        {
            if (is_open == 1)
            {
                fwrite(buffer, 512, 1, img); // able to use img now
            }
        }
    }
    fclose(img);
    fclose(card);
}