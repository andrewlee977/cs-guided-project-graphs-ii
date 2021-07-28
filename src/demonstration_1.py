"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

```plaintext
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```

Notes:

- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
def flood_fill(image, sr, sc, new_color):
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int

    Output:
    List[List[int]]
    """
    # Your code here
    # get the mex rows
    MAX_ROWS = len(image)
    # get the max cols
    MAX_COLS = len(image[0])
    # extract the current color of the image at sr and sc
    current_color = image[sr][sc]
    # if current color is the same as the new color then return the image
    if current_color == new_color:
      return image
    # curry a dfs function inside the flood fill
    def dfs(row, col):
      # if the image at the current row and current col is equal to the current color
      if image[row][col] == current_color:
        # set the image at current row and current col to the new color
        image[row][col] = new_color

        # if the row is gereater than or equal to 1.
        if row >= 1:
          # call dfs on row - 1 and col
          dfs(row - 1, col)
        # check if the row + 1 is less than the max rows.
        if row + 1 < MAX_ROWS:
          # call dfs on row + 1 and col
          dfs(row + 1, col)
        # if col is greater than or equal to 1.
        if col >= 1:
          # call dfs on row and the col - 1
          dfs(row, col - 1)
        # check if col + 1 is less than max cols.
        if col + 1 < MAX_COLS:
          # call dfs on row and the col + 1
          dfs(row, col + 1)
    # call dfs with sr and sc
    dfs(sr, sc)

    # return the image
    return image



