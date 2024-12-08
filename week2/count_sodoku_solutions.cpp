#include <stdio.h>

int count = 0;

// Ham kiem tra rang buoc (co the dat so n vao vi tri [r][c] hay khong)
int contraints(int r, int c, int a[9][9], int n) {
    // Kiem tra hang va cot xem so n da ton tai hay chua
    for (int i = 0; i < 9; i++) {
        if (a[r][i] == n || a[i][c] == n) {
            return 0; // Khong the dat n neu da ton tai
        }
    }

    // Kiem tra o vuong 3x3 chua vi tri [r][c]
    int I = r / 3; // Tinh chi so hang cua o 3x3
    int J = c / 3; // Tinh chi so cot cua o 3x3
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (a[3 * I + i][3 * J + j] == n) {
                return 0; // Khong the dat n neu da ton tai
            }
        }
    }

    return 1; // Co the dat so n vao vi tri [r][c]
}

// Ham backtracking de thu tung gia tri va dem so loi giai
void back_track(int r, int c, int a[9][9]) {

    // Truong hop co so: Neu da duyet xong toan bo bang
    if (r == 9) {
        count++; // Tang so luong loi giai
        return;
    }

    // Neu vi tri [r][c] da co so, chuyen sang vi tri tiep theo
    if (a[r][c] != 0) {
        if (c == 8) { 
            // Neu cot cuoi cung, chuyen xuong hang tiep theo
            back_track(r + 1, 0, a);
        } else { 
            // Chuyen sang cot tiep theo trong cung hang
            back_track(r, c + 1, a);
        }
    } else { 
        // Neu vi tri [r][c] trong, thu cac gia tri tu 1 den 9
        for (int i = 1; i <= 9; i++) {
            if (contraints(r, c, a, i)) { 
                // Neu gia tri i thoa man rang buoc, dat i vao vi tri [r][c]
                a[r][c] = i; 

                if (c == 8) {
                    // Neu cot cuoi cung, chuyen xuong hang tiep theo
                    back_track(r + 1, 0, a);
                } else {
                    // Chuyen sang cot tiep theo
                    back_track(r, c + 1, a);
                }

                // Hoan tac (backtrack) de thu gia tri khac
                a[r][c] = 0; 
            }
        }
    }
}

int main() {
    int a[9][9];

    // Nhap du lieu bang Sudoku (9x9)
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    // Bat dau tim loi giai tu o dau tien
    back_track(0, 0, a);

    // In ra so luong loi giai tim duoc
    printf("%d\n", count);

    return 0;
}

