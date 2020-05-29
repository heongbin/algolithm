#한 웹페이지당 기본점수, 외부링크수, 링크점수 / 최종 매칭 점수.

#한 웹페이지의 기본점수는 해당하는검색어와 일치하는 단어의 갯수(대소문자구분x)

#외부링크수는 그페이지에서 다른페이지에 뻗어잇는 링크들의 개수.

#링크점수는 해당웹페이지로 링크를 건 다른 페이지들의 (기본점수/외부링크수)

#한웹페이지의 매칭점수는 그페이지의 (기본점수+링크점수)
from collections import defaultdict
final_list=[]
word="Muzi"
#pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
for page in range(len(pages)):
    tmp_data_lst=[]
    head_st=pages[page].find("<head>") #68
    head_ed=pages[page].find("</head>")
    head_sector=pages[page][head_st+6:head_ed]
    page_url_st=head_sector.find("https")
    page_url_ed=head_sector.find("/>")

    page_url=head_sector[page_url_st:page_url_ed-1]

    body_st=pages[page].find("<body")
    body_end=pages[page].find("</body")

    body_sector=pages[page][body_st+6:body_end+1]
    copy_body_sector=body_sector[:]


    ahref_list=[] #외부링크로 연결할 사이트목록.
    body_list=[]

    ahref_start_index = copy_body_sector.find("<a href") #외부링크 사이트 얻어오기

    if ahref_start_index!=-1:
        while True: #a href 존재
            #if ahref_start_index==0: #외부링크 사이트 얻어오기
            if ahref_start_index==-1:
                break
            ahref_end_index=copy_body_sector.find("</a>")+4
            ahref_tmp_sector=copy_body_sector[ahref_start_index:ahref_end_index]
            tmp_front=ahref_tmp_sector.find("=")+2
            tmp_last=ahref_tmp_sector.find(">")-2
            ahref_tmp_sector=ahref_tmp_sector[tmp_front:tmp_last+1] #
            ahref_list.append(ahref_tmp_sector)
            copy_body_sector=copy_body_sector[ahref_end_index:]
            ahref_start_index = copy_body_sector.find("<a href")  # 외부링크 사이트 얻어오기

    cnt=0
    find_word=[]
    word=word.lower()
    body_sector=body_sector.lower()

    find_index_start=body_sector.find(word)

    if find_index_start!=-1:
        while True:
            if find_index_start==-1:
                break
            tmp_front=body_sector[find_index_start-1]
            print(body_sector)
            tmp_last=body_sector[find_index_start+len(word)]

            if tmp_front.isalpha()==False and tmp_last.isalpha()==False:
                cnt+=1
            body_sector=body_sector[find_index_start+len(word)-1:]
            print(body_sector)
            find_index_start=body_sector.find(word)


    tmp_data_lst.append(page_url)
    tmp_data_lst.append(ahref_list)
    tmp_data_lst.append(cnt)
    final_list.append(tmp_data_lst)



dic=defaultdict(int)
for i in range(len(final_list)):
    for j in range(len(final_list)):
        for link_url in final_list[j][1]:
            if final_list[i][0]==link_url:
                dic[final_list[i][0]]+=final_list[j][2]/len(final_list[j][1])
                break
    dic[final_list[i][0]]+=final_list[i][2]

max_key=sorted(dic,key=lambda x : dic[x])
max_key_list=[]
for i in range(len(final_list)):
    if max_key[-1]==final_list[i][0]:
        max_key_list.append(i)
print(max_key_list[0])

answer=0
for i in range(len(final_list)):
    if final_list[i][0]==max_key:
        answer=i
        break





