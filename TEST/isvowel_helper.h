// is vowel
int isvowel(char c)
{
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void convert(char *str_input, char *str_output, int str_len)
{
    for (int i = 0, j = 0; i < str_len; i++, j++)
    {
        if (isvowel(str_input[i]))
        {
            str_output[j] = str_input[i];
            str_output[j+1] = 'v';
            str_output[j+2] = str_input[i];
            j += 2;
        }
        else
        {
            str_output[j] = str_input[i];
        }
    }
}