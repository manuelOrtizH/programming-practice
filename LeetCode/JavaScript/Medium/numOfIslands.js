// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/number-of-islands/

const LAND = '1';
const WATER = '0';

const dfs = (grid, i, j) => {
    if (i < 0 || j < 0) return;
    if (i >= grid.length || j >= grid[0].length) return;
    if (grid[i][j] != LAND ) return;
    
    grid[i][j] = WATER;
    dfs(grid, i, j-1);
    dfs(grid, i, j+1);
    dfs(grid, i-1, j);
    dfs(grid, i+1, j);
    return;
    
    
}

const numIslands = grid => {
    let islands = 0;
    let i = 0;
    let j = 0;
    while (i < grid.length){
        while (j < grid[i].length){
            if (grid[i][j] == LAND){
                islands++;
                dfs(grid, i, j);
            }else { j++; }
        }
        j = 0;
        i++;
        
    }
    return islands;
};