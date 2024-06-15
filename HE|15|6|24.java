


/* Problem

Bob has a playlist of

songs, each song has a singer associated with it (denoted by an integer)

Favourite singer of Bob is the one whose songs are the most on the playlist

Count the number of Favourite Singers of Bob

Input Format 

The first line contains an integer 

, denoting the number of songs in Bob's playlist.

The following input contains
integers,  integer denoting the singer of the 

 song.

Output Format

Output a single integer, the number of favourite singers of Bob

Note: Use 64 bit data type */









// Sample C code
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
int n;
scanf("%d", &n);
char songs[n][100]; // Assuming a maximum of 100 characters per song

for (int i = 0; i < n; i++) {
scanf("%s", songs[i]);
}

// Find the maximum frequency of any song and count how many songs have that frequency
int max = 0, count = 0;
for (int i = 0; i < n; i++) {
int freq = 1;
if (songs[i][0] == '\0') continue; // Skip if the song is empty

for (int j = i + 1; j < n; j++) {
if (strcmp(songs[i], songs[j]) == 0) {
freq++;
songs[j][0] = '\0'; // Mark the duplicate song as empty
}
}

if (freq > max) {
max = freq;
count = 1;
} else if (freq == max) {
count++;
}
}

printf("%d\n", count);

return 0;
}
