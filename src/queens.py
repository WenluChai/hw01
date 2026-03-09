def solve_n_queens(n):
    """求解N皇后问题，返回所有合法布局"""
    solutions = []
    def backtrack(row, cols, diag1, diag2, path):
        if row == n:
            solutions.append(path.copy())
            return
        for col in range(n):
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                path.append(col)
                backtrack(row + 1, cols, diag1, diag2, path)
                # 回溯
                path.pop()
                diag2.remove(row + col)
                diag1.remove(row - col)
                cols.remove(col)
    backtrack(0, set(), set(), set(), [])
    return solutions

def print_board(solution):
    """格式化打印棋盘"""
    n = len(solution)
    for col in solution:
        print('.' * col + 'Q' + '.' * (n - col - 1))

# 测试入口（可选）
if __name__ == "__main__":
    res = solve_n_queens(4)
    print(f"4皇后问题共有{len(res)}种解法：")
    for i, sol in enumerate(res):
        print(f"解法{i+1}：")
        print_board(sol)
        print()