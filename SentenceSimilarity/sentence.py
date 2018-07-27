#encoding=utf-8

from zhcnSegment import Seg

class Sentence(object):
	
    def __init__(self,sentence,seg,id = 0):
        self.id = id      #对象变量
        self.origin_sentence = sentence
        self.cuted_sentence = self.cut(seg)
				
    # 对句子分词
    def cut(self,seg):
        return seg.cut_for_search(self.origin_sentence) #类的继承
				
    # 获取切词后的词列表
    def get_cuted_sentence(self):
        return self.cuted_sentence

    # 获取原句子
    def get_origin_sentence(self):
        return self.origin_sentence
		
    # 设置该句子得分
    def set_score(self,score):
        self.score = score
		