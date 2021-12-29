from typing import List














def pascal(N: int) -> List[int]:


    current_row = [1]

    for _ in range(N - 1):
        new_row = [1]

        for i in range(0,len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i +1])
        new_row.append(1)
        current_row = new_row


    

    return current_row

















