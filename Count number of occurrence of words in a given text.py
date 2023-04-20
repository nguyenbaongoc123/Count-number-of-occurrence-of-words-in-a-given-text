#!/usr/bin/env python
# coding: utf-8

# Viết chương trình đếm số lần xuất hiện của một từ trong một văn bản nhất định (đã cho sẵn)

# In[7]:


def count_words(word,mes):
    mes.lower()
    mes.strip()
    text_list=list(mes.split())
    test_set=set(text_list)
    num_words={}
    #for word in test_set:
    num_words[word]=text_list.count(word)
    num_words=num_words.get(word,0)
    return num_words
message='''Những siêu máy tính cực mạnh đóng vai trò cốt lõi đối với NASA, 
từ mô phỏng khí hậu và thời tiết toàn cầu tới phát triển công nghệ hạ cánh trên hành tinh khác.

1. Thiết kế taxi bay an toàn và hiệu quả

Sử dụng siêu máy tính của NASA, các nhà nghiên cứu mô phỏng hiệu suất khí động học của một số cấu hình taxi bay 
hứa hẹn chở người và hàng hóa ở đô thị và ngoại ô trong tương lai. Những mô phỏng độ phức tạp cao sẽ được sử dụng
để thiết kế taxi bay hay còn gọi là phương tiện Advanced Air Mobility (AAM) an toàn, êm ái và hiệu quả.

NASA cũng đóng vai trò quan trọng trong phát triển AAM bằng cách xác định lĩnh vực nghiên cứu chủ chốt 
và khái niệm hóa thiết kế của AAM. Mô phỏng gần đây tập trung vào hiệu suất của cánh nghiêng và rotor đơn.
Mô phỏng tiến hành trên các siêu máy tính như Aitken ở cơ sở Siêu máy tính cao cấp NASA (NAS) 
tại Trung tâm nghiên cứu Ames trong thung lũng Silicon, California, được giải quyết chỉ trong vài ngày. 
Tìm hiểu cấu trúc dòng chảy ở máy bay cánh quạt là chìa khóa để đạt mục tiêu về hiệu suất và độ ồn.'''
print(count_words("do",message))


# In[ ]:




