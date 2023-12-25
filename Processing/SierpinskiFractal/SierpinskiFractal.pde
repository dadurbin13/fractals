int depth = 7; // Set your desired depth level here
float margin = 10; // Margin from the top and bottom of the screen

void settings() {
    fullScreen(); // Set the sketch to full-screen mode
}

void setup () {
  noStroke();
  fill(50);
}

void draw() {
 background(255);

 // Adjust the size of the triangle to fit the screen with margins
 float availableHeight = height - 2 * margin;
 float len = 2 * availableHeight / sqrt(3); // Adjusted length of the base of the triangle

 // Calculate the starting position
 float startX = (width - len) / 2;
 float startY = height - margin;

 divide(startX, startY, len, 1, depth);
}

void divide(float x, float y, float l, int lvl, int max) {
 if(lvl == max) {
   tri(x, y, l);
 } else {
   divide(x, y, l / 2, lvl + 1, max);
   divide(x + l / 2, y, l / 2, lvl + 1, max);
   divide(x + l / 4, y - sin(PI / 3) * l / 2, l / 2, lvl + 1, max);
 }
}

void tri(float x, float y, float l) {
 triangle(x, y, x + l / 2, y - sin(PI / 3) * l, x + l, y); 
}
