#include "helpers.h"
#include "math.h"
#include "stdio.h"
#include "stdlib.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float r = image[i][j].rgbtRed;
            float g = image[i][j].rgbtGreen;
            float b = image[i][j].rgbtBlue;

            float c = (r + g + b) / 3;

            image[i][j].rgbtRed = round(c);
            image[i][j].rgbtGreen = round(c);
            image[i][j].rgbtBlue = round(c);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float r = image[i][j].rgbtRed;
            float g = image[i][j].rgbtGreen;
            float b = image[i][j].rgbtBlue;

            float red = .393 * r + .769 * g + .189 * b;
            float green = .349 * r + .686 * g + .168 * b;
            float blue = .272 * r + .534 * g + .131 * b;

            if (red > 255)
            {
                red = 255;
            }

            if (green > 255)
            {
                green = 255;
            }

            if (blue > 255)
            {
                blue = 255;
            }

            image[i][j].rgbtRed = round(red);
            image[i][j].rgbtGreen = round(green);
            image[i][j].rgbtBlue = round(blue);
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // initialize new temp array with RGB struct
    RGBTRIPLE newimage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //flip the j value
            int fliph = (width - 1 - j);

            // getting RGB values of original
            newimage[i][fliph] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // place the newly flipped values into the old array
            image[i][j] = newimage[i][j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE newimage[height][width]; // Gets mirror image to work on

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            newimage[i][j] = image[i][j]; 
        }
    }                                   // done with image mapping
    
    for (int i = 0; i < height; i++) // goes over entire image i for rows (height), j for columns (width)
    {
        for (int j = 0; j < width; j++)
        {
            float sumr = 0; // initalize the sum values of the rgbt's
            float sumg = 0;
            float sumb = 0;
            int pixel_count = 0; // used to count how many pixels are done for each rotation
            
            for (int k = -1; k < 2; k++) // checks each pixel within -1 to + 1 of each [i]  (ie left to right)
            {
                for (int l = -1; l < 2; l++) // checks each pixel withint -1 to +1 of each j pixel (ie up to down)
                {
                    if (i + k >= 0  && j + l >= 0 && i + k <= height - 1 && j + l <= width - 1) // if statement to check
                    {                                                                           // if pixel check is
                        sumr = newimage[i + k][j + l].rgbtRed + sumr;                           // within bounds
                        sumg = newimage[i + k][j + l].rgbtGreen + sumg;
                        sumb = newimage[i + k][j + l].rgbtBlue + sumb; 
                        pixel_count++; //adds one to the pixel count to divide by within each [i][j] loop
                    }
                }
            }
            
            image[i][j].rgbtRed = round(sumr / pixel_count);
            image[i][j].rgbtGreen = round(sumg / pixel_count);
            image[i][j].rgbtBlue = round(sumb / pixel_count);
        }
    }
    return;
}