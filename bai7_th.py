def find_winners(N, M, K, teams):
    winners = []

    for i in range(N):
        current_team = teams[i]
        current_sum = 0

        for j in range(N):
            if teams[j] == current_team:
                current_sum += (K % M) + 1  # Cộng số trong khoảng [1, K]
            else:
                current_sum += 1

            if current_sum >= M:
                winners.append(current_team)
                break

        # Thêm kiểm tra ở đây
        if current_sum < M:
            winners.append(1 - current_team)
        else:
            winners.append(current_team)

    return winners

# Đọc input
N, M, K = map(int, input().split())
teams = list(map(int, input().split()))

# Tìm và in ra đội chiến thắng cho mỗi người chơi đầu tiên
result = find_winners(N, M, K, teams)
print(" ".join(map(str, result)))
