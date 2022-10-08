// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/flood-fill/

const floodFill = (image, sr, sc, color) => {
    if (image[sr][sc] == color) return image; //Nothing to change
        
    return floodFillHelper(image,sr,sc,color, image[sr][sc], image.length, image[0].length);
              
};

const floodFillHelper = (image,sr,sc,color,startingPixel, M, N) => {
    if ((sr < 0) || (sc < 0)) return image;
    if ((sr >= M) || (sc >= N)) return image;
    if (image[sr][sc] != startingPixel || image[sr][sc] == color) return image;
    
    image[sr][sc] = color;
    // Move in the 4 directions only
    //Left
    floodFillHelper(image, sr, sc-1, color, startingPixel, M, N);
    //Right
    floodFillHelper(image, sr, sc+1, color, startingPixel, M, N);
    //Up
    floodFillHelper(image, sr+1, sc, color, startingPixel, M, N);
    //Down
    floodFillHelper(image, sr-1, sc, color, startingPixel, M, N);
    
    return image;
    
};