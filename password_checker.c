#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to check password strength
int checkStrength(char password[]) {
    int length = strlen(password);
    int hasLower = 0, hasUpper = 0, hasDigit = 0, hasSpecial = 0;

    for (int i = 0; i < length; i++) {
        if (islower(password[i])) hasLower = 1;
        else if (isupper(password[i])) hasUpper = 1;
        else if (isdigit(password[i])) hasDigit = 1;
        else hasSpecial = 1;
    }

    int score = hasLower + hasUpper + hasDigit + hasSpecial;

    if (length >= 12 && score == 4) return 3; // Strong
    else if (length >= 8 && score >= 3) return 2; // Medium
    else return 1; // Weak
}

int main() {
    char password[100];
    printf("Enter your password: ");
    scanf("%s", password);

    int strength = checkStrength(password);

    if (strength == 3) {
        printf("Strength: Strong\n");
        printf("Good job! Your password is secure.\n");
    } else if (strength == 2) {
        printf("Strength: Medium\n");
        printf("Recommendation: Add more characters and include symbols.\n");
    } else {
        printf("Strength: Weak\n");
        printf("Recommendation: Use at least 8 characters with uppercase, lowercase, digits, and symbols.\n");
    }

    return 0;
}
