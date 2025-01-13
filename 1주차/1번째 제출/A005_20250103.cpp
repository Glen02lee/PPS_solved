#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* skill, const char* skill_trees[], size_t skill_trees_len) {
    int answer = 0;
    size_t skill_len = strlen(skill);
    
    for (size_t i = 0; i < skill_trees_len; i++) {
        const char* skill_tree = skill_trees[i];
        size_t skill_tree_len = strlen(skill_tree);
        int skill_index = 0;
        bool is_valid = true;
        
        for (size_t j = 0; j < skill_tree_len; j++) {
            char current_skill = skill_tree[j];
            char* pos = strchr(skill, current_skill);
            
            if (pos) {
                int required_index = pos - skill;
                if (required_index > skill_index) {
                    is_valid = false;
                    break;
                }
                skill_index++;
            }
        }
        
        if (is_valid) {
            answer++;
        }
    }
    
    return answer;
}
/*
스킬트리에 맞게 스킬을 배워갈 수 있는지 파악한다고 이해한 문제
만약 알파벳순서가 스킬트리라면, 알파벳 순서는 스킬트리의 순서가 된다.
따라서 문제는 그저 순서대로인지 아닌지를 판별하는 것.
애매한것은 알파벳을 예로 들었을때, a - c -d 라고 있을 때, b를 건너뛰었지만
"순서대로"에서 벗어나진 않았다. 이 부분을 염두에두고 코딩하였다.
그래서 현재 스킬이 스킬트리에 포함되는지와, 순서대로인지만 파악하면 된다고 생각했다.
*/