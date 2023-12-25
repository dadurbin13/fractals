float len = 2000;
int depth = 7; // Set your desired depth level here

void settings() {
    fullScreen();
}

void setup () {
  noStroke();
  fill(50);
}

void draw() {
 background(255);
 float adjustedX = width / 2 - len / 2;
 float adjustedY = height / 2 + sin(PI / 3) * len / 2;
 divide(adjustedX, adjustedY, len, 1, depth);
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
