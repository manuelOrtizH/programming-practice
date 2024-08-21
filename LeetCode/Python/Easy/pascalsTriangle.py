class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # fill with 1's the pascal triangle
        pascal_triangle = [[1 for x in range(1,i+1)] for i in range(1,numRows+1)]
        if numRows > 2:
            for i in range(2,len(pascal_triangle)):
                for j in range(1, len(pascal_triangle[i]) - 1):
                    pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]

        return pascal_triangle

def main():
    sol = Solution()
    numRows = 5
    print(sol.generate(numRows))

if __name__ == "__main__":
    main()