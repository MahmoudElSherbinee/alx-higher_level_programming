#include <stdio.h>

int main(void)
{
    for (int x = 0; x < 10; x++)
    {
        for (int y = 0, (y < 10) && (y != x); y++)
        {
            if (x < y)
            {
                printf("%d%d", x, y);
            }
        }
    }
}