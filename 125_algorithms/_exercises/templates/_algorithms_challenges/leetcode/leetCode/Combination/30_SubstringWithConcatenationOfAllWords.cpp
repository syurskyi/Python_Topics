/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-12 18:58:58
 */

c.. Solution {
public:
    // Easy to understand but slow.
    vector<int> findSubstring(string s, vector<string>& words) {
        int s_len = s.size();
        int w_len = words.size();
        __(s_len __ 0 || w_len__0){
            r_ {};
        }

        int wl = words[0].size();
        int str_len = w_len * words[0].size();
        unordered_map<string, int> word_cnt;
        ___(auto &w: words){
            word_cnt[w] += 1;
        }
        vector<int> ans;
        ___(int i=0; i<s_len-str_len+1; i++){
            unordered_map<string, int> tmp_cnt;
            int j=0;
            _____(j<w_len){
                string cur_word = s.substr(i+j*wl, wl);
                __(word_cnt.find(cur_word)__word_cnt.end()){
                    ______;
                }
                else{
                    tmp_cnt[cur_word] ++;
                    __(tmp_cnt[cur_word] > word_cnt[cur_word]){
                        ______;
                    }
                }
                j++;
            }
            __(j __ w_len){
                ans.push_back(i);
            }
        }
        r_ ans;
    }
};


c.. Solution_2 {
public:
    /*
    Use hashmap and two point.

    Travel all the words combinations to maintain a slicing window.
    There are wl(word len) times travel, each time n/wl words:
    mostly 2 times travel for each word:
        one left side of the window, the other right side of the window
    So, time complexity O(wl * 2 * N/wl) = O(2N)
    Refer to:
    https://discuss.leetcode.com/topic/6617/an-o-n-solution-with-detailed-explanation
    */
    vector<int> findSubstring(string s, vector<string>& words) {
        int s_len = s.size();
        int total_cnt = words.size();
        __(s_len __ 0 || total_cnt__0){
            r_ {};
        }

        int w_len = words[0].size();
        unordered_map<string, int> words_cnt;
        ___(auto &w: words){
            words_cnt[w] ++;
        }

        vector<int> ans;
        ___(int i=0; i<w_len; i++){
            int left=i, count=0;
            unordered_map<string, int> candidate_cnt;
            ___(int j=i; j<=s_len-w_len; j+=w_len){
                string cur_str = s.substr(j, w_len);
                __(words_cnt.find(cur_str) != words_cnt.end()){
                    candidate_cnt[cur_str] ++;
                    count += 1;
                    __(candidate_cnt[cur_str] > words_cnt[cur_str]){
                        // A more word, advance the window left side possiablly
                        _____(candidate_cnt[cur_str] > words_cnt[cur_str]){
                            string left_str = s.substr(left, w_len);
                            candidate_cnt[left_str] --;
                            left += w_len;
                            count --;
                        }
                    }
                    // come to a result
                    __(count __ total_cnt){
                        ans.push_back(left);
                        candidate_cnt[s.substr(left, w_len)] --;
                        count --;
                        left += w_len;
                    }
                }
                else{
                    left = j+w_len;
                    candidate_cnt _ # dict;
                    count = 0;
                }
            }
        }
        r_ ans;
    }
};


/*
""
[]
"barfoothefoobarman"
["foo", "bar"]
"barfoofoobarthefoobarman"
["bar","foo","the"]
*/
