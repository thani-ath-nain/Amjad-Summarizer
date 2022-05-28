import stanza, math


class AmjadSummarizer:
    def __init__(self, text):
        self.URDU_DIACRITICS = ['ِ', 'ٰ', 'ُ', 'ٍ', 'ً', 'َ']
        self.URDU_DIGIT = ['۶', '۴', '۵', '۸', '۲', '۰', '۷', '۹', '۳', '۱']
        self.URDU_PUNCTUATIONS = ['\200F', '\u200f','؛', '۔', '٫', '٪', '؟', '،', ')', '(', '{', '}', '۔']
        self.URDU_EXTRA_CHARACTER = [1623,1538, 1617,1537,1551,1539, 1624, 1550,1622,1644,1555,1620,1619,1552,1554,1556,1612,1557,1549,1553,1618,1536]
        self.URDU_ALPHABET = ['أ','خ','ۃ', 'ز', 'ہ', 'ظ', 'چ', 'ع', 'ش','ن', 'ء','ق','ژ','م','ج','ب', 'ک', 'ٹ', 'ؤ','غ', 'ح', 'گ','ت', 'ڈ', 'ض','ئ','ر','ث', 'ڑ', 'ذ', 'س', 'ط', 'ی', 'ف', 'ۂ', 'پ', 'ص', 'ا','ے', 'ۓ', 'و', 'آ', 'ھ','د','ل','ں']
        self.URDU_STOPWORDS = ["آئی","آئے","آج","آخر","آخرکبر","آدهی","آًب","آٹھ","آیب","اة","اخبزت","اختتبم","ادھر","ارد","اردگرد","ارکبى","اش","اضتعوبل","اضتعوبلات","اضطرذ","اضکب","اضکی","اضکے","اطراف","اغیب","افراد","الگ","اور","اوًچب","اوًچبئی","اوًچی","اوًچے","اى","اً","اًذر","اًہیں","اٹھبًب","اپٌب","اپٌے","اچھب","اچھی","اچھے","اکثر","اکٹھب","اکٹھی","اکٹھے","اکیلا","اکیلی","اکیلے","اگرچہ","اہن","ایطے","ایک","ب","ت","تبزٍ","تت","تر","ترتیت","تریي","تعذاد","تن","تو","توبم","توہی","توہیں","تٌہب","تک","تھب","تھوڑا","تھوڑی","تھوڑے","تھی","تھے","تیي","ثب","ثبئیں","ثبترتیت","ثبری","ثبرے","ثبعث","ثبلا","ثبلترتیت","ثبہر","ثدبئے","ثرآں","ثراں","ثرش","ثعذ","ثغیر","ثلٌذ","ثلٌذوثبلا","ثلکہ","ثي","ثٌب","ثٌبرہب","ثٌبرہی","ثٌبرہے","ثٌبًب","ثٌذ","ثٌذکرو","ثٌذکرًب","ثٌذی","ثڑا","ثڑوں","ثڑی","ثڑے","ثھر","ثھرا","ثھراہوا","ثھرپور","ثھی","ثہت","ثہتر","ثہتری","ثہتریي","ثیچ","ج","خب","خبرہب","خبرہی","خبرہے","خبهوظ","خبًب","خبًتب","خبًتی","خبًتے","خبًٌب","خت","ختن","خجکہ","خص","خططرذ","خلذی","خو","خواى","خوًہی","خوکہ","خٌبة","خگہ","خگہوں","خگہیں","خیطب","خیطبکہ","در","درخبت","درخہ","درخے","درزقیقت","درضت","دش","دفعہ","دلچطپ","دلچطپی","دلچطپیبں","دو","دور","دوراى","دوضرا","دوضروں","دوضری","دوضرے","دوًوں","دکھبئیں","دکھبتب","دکھبتی","دکھبتے","دکھبو","دکھبًب","دکھبیب","دی","دیب","دیتب","دیتی","دیتے","دیر","دیٌب","دیکھو","دیکھٌب","دیکھی","دیکھیں","دے","ر","راضتوں","راضتہ","راضتے","رریعہ","رریعے","رکي","رکھ","رکھب","رکھتب","رکھتبہوں","رکھتی","رکھتے","رکھی","رکھے","رہب","رہی","رہے","ز","زبصل","زبضر","زبل","زبلات","زبلیہ","زصوں","زصہ","زصے","زقبئق","زقیتیں","زقیقت","زکن","زکویہ","زیبدٍ","صبف","صسیر","صفر","صورت","صورتسبل","صورتوں","صورتیں","ض","ضبت","ضبتھ","ضبدٍ","ضبرا","ضبرے","ضبل","ضبلوں","ضت","ضرور","ضرورت","ضروری","ضلطلہ","ضوچ","ضوچب","ضوچتب","ضوچتی","ضوچتے","ضوچو","ضوچٌب","ضوچی","ضوچیں","ضکب","ضکتب","ضکتی","ضکتے","ضکٌب","ضکی","ضکے","ضیذھب","ضیذھی","ضیذھے","ضیکٌڈ","ضے","طرف","طریق","طریقوں","طریقہ","طریقے","طور","طورپر","ظبہر","ع","عذد","عظین","علاقوں","علاقہ","علاقے","علاوٍ","عووهی","غبیذ","غخص","غذ","غروع","غروعبت","غے","فرد","فی","ق","قجل","قجیلہ","قطن","لئے","لا","لازهی","لو","لوجب","لوجی","لوجے","لوسبت","لوسہ","لوگ","لوگوں","لڑکپي","لگتب","لگتی","لگتے","لگٌب","لگی","لگیں","لگے","لی","لیب","لیٌب","لیں","لے","ه","هتعلق","هختلف","هسترم","هسترهہ","هسطوش","هسیذ","هطئلہ","هطئلے","هطبئل","هطتعول","هطلق","هعلوم","هػتول","هلا","هوکي","هوکٌبت","هوکٌہ","هٌبضت","هڑا","هڑًب","هڑے","هکول","هگر","هہرثبى","هیرا","هیری","هیرے","هیں","و","وار","والے","وٍ","ًئی","ًئے","ًب","ًبپطٌذ","ًبگسیر","ًطجت","ًقطہ","ًو","ًوخواى","ًکبلٌب","ًکتہ","ًہ","ًہیں","ًیب","ًے","ٓ آش","ٹھیک","پبئے","پبش","پبًب","پبًچ","پر","پراًب","پطٌذ","پل","پورا","پوچھب","پوچھتب","پوچھتی","پوچھتے","پوچھو","پوچھوں","پوچھٌب","پوچھیں","پچھلا","پھر","پہلا","پہلی","پہلےضی","پہلےضے","پہلےضےہی","پیع","چبر","چبہب","چبہٌب","چبہے","چلا","چلو","چلیں","چلے","چکب","چکی","چکیں","چکے","چھوٹب","چھوٹوں","چھوٹی","چھوٹے","چھہ","چیسیں","ڈھوًڈا","ڈھوًڈلیب","ڈھوًڈو","ڈھوًڈًب","ڈھوًڈی","ڈھوًڈیں","ک","کئی","کئے","کب","کبفی","کبم","کت","کجھی","کرا","کرتب","کرتبہوں","کرتی","کرتے","کرتےہو","کررہب","کررہی","کررہے","کرو","کرًب","کریں","کرے","کطی","کل","کن","کوئی","کوتر","کورا","کوروں","کورٍ","کورے","کوطي","کوى","کوًطب","کوًطی","کوًطے","کھولا","کھولو","کھولٌب","کھولی","کھولیں","کھولے","کہ","کہب","کہتب","کہتی","کہتے","کہو","کہوں","کہٌب","کہی","کہیں","کہے","کی","کیب","کیطب","کیطرف","کیطے","کیلئے","کیوًکہ","کیوں","کیے","کے","کےثعذ","کےرریعے","گئی","گئے","گب","گرد","گروٍ","گروپ","گروہوں","گٌتی","گی","گیب","گے","ہر","ہن","ہو","ہوئی","ہوئے","ہوا","ہوبرا","ہوبری","ہوبرے","ہوتب","ہوتی","ہوتے","ہورہب","ہورہی","ہورہے","ہوضکتب","ہوضکتی","ہوضکتے","ہوًب","ہوًی","ہوًے","ہوچکب","ہوچکی","ہوچکے","ہوگئی","ہوگئے","ہوگیب","ہوں","ہی","ہیں","ہے","ی","یقیٌی","یہ","یہبں"]
        self.text = text
        self.nlp = stanza.Pipeline(lang='ur', processors='tokenize')
        self.doc = self.nlp(self.text)
        self.sentences = self.doc.sentences
        self.totalDocuments = len(self.sentences)
    

    def summarize(self):
        frequencyMatrix = self.createFrequencyMatrix(self.sentences)
        tfMatrix = self.createTFMatrix(frequencyMatrix)
        countDocPerWords = self.createDocumentsPerWords(frequencyMatrix)
        idfMatrix = self.createIdfMatrix(frequencyMatrix, countDocPerWords, self.totalDocuments)
        tfIdfMatrix = self.createTfIdfMatrix(tfMatrix, idfMatrix)
        sentenceScores = self.scoreSentences(tfIdfMatrix)
        threshold = self.findAverageScore(sentenceScores)
        return self.generateSummary(self.sentences, sentenceScores, 0.6 * threshold)

    def createFrequencyMatrix(self, sentences):
        frequencyMatrix = {}
        for sentence in sentences:
            freqTable = {}
            words = [token.text for token in sentence.tokens]
            for word in words:
                if ( word in self.URDU_STOPWORDS or word in self.URDU_EXTRA_CHARACTER or
                    word in self.URDU_EXTRA_CHARACTER or word in self.URDU_PUNCTUATIONS or word in self.URDU_DIACRITICS):
                    continue

                if word in freqTable:
                    freqTable[word] += 1
                else:
                    freqTable[word] = 1
            
            frequencyMatrix[sentence.text[:15]] = freqTable
        return frequencyMatrix
    

    def createTFMatrix(self, freqMatrix):
        tfMatrix = {}

        for sent, fTable in freqMatrix.items():
            tfTable = {}

            countOfWordsSentence = len(fTable)
            for word, count in fTable.items():
                tfTable[word] = count / countOfWordsSentence

            tfMatrix[sent] = tfTable

        return tfMatrix

    
    def createDocumentsPerWords(self, freqMatrix):
        wordPerDocTable = {}

        for sent, fTable in freqMatrix.items():
            for word, count in fTable.items():
                if word in wordPerDocTable:
                    wordPerDocTable[word] += 1
                else:
                    wordPerDocTable[word] = 1

        return wordPerDocTable
    
    def createIdfMatrix(self, freqMatrix, countDocPerWords, totalDocuments):
        idfMatrix = {}

        for sent, fTable in freqMatrix.items():
            idfTable = {}

            for word in fTable.keys():
                idfTable[word] = math.log10(totalDocuments / float(countDocPerWords[word]))

            idfMatrix[sent] = idfTable

        return idfMatrix

    def createTfIdfMatrix(self, tfMatrix, idfMatrix):
        tfIdfMatrix = {}

        for (sent1, fTable1), (sent2, fTable2) in zip(tfMatrix.items(), idfMatrix.items()):

            tfIdfTable = {}

            for (word1, value1), (word2, value2) in zip(fTable1.items(),
                                                        fTable2.items()):  
                tfIdfTable[word1] = float(value1 * value2)

            tfIdfMatrix[sent1] = tfIdfTable

        return tfIdfMatrix
    

    def scoreSentences(self, tfIdfMatrix) -> dict:
        """
        score a sentence by its word's TF
        Basic algorithm: adding the TF frequency of every non-stop word in a sentence divided by total no of words in a sentence.
        :rtype: dict
        """

        sentenceValue = {}

        for sent, fTable in tfIdfMatrix.items():
            totalScorePerSentence = 0

            countWordsInSentence = len(fTable)
            for word, score in fTable.items():
                totalScorePerSentence += score

            sentenceValue[sent] = totalScorePerSentence / countWordsInSentence

        return sentenceValue

    def findAverageScore(self, sentenceValue) -> int:
        """
        Find the average score from the sentence value dictionary
        :rtype: int
        """
        sumValues = 0
        for entry in sentenceValue:
            sumValues += sentenceValue[entry]

        # Average value of a sentence from original summary_text
        average = (sumValues / len(sentenceValue))

        return average

    def generateSummary(self, sentences, sentenceValue, threshold):
        sentenceCount = 0
        summary = ''

        for sentence in sentences:
            if sentence.text[:15] in sentenceValue and sentenceValue[sentence.text[:15]] >= (threshold):
                summary += " " + sentence.text
                sentenceCount += 1

        return summary





text = """
ماہرین کا خیال ہے کہ پھل اور سبزیاں انسانی خوراک کا لازمی جز ہونی چاہئیں ۔
ان میں موجود وٹامنز اور معدنیات صحت مند رہنے اور بیماریوں سے بچاؤ کے لئے معاون ثابت ہوتی ہیں ۔
سبزیوں اور پھلوں میں موجود دوسرے اجزاء اینٹی آکسیڈنٹس ، پیتھو کیکیکلز اور دیگر مرکبات کینسر ، ذیابیطس اور دل کے امراض سے محفوظ رکھتے ہیں ۔
سبزیوں اور پھلوں کی ڈھیروں اقسام موجود ہیں ۔
ماہرین کا اصرار ہے کہ روزانہ پانچ مختلف اقسام کی سبزیاں اور دو اقسام کے پھل انسانی خوراک کا حصہ ہونی چاہئیں ۔
ماہرین کہتے ہیں کہ ترقی پزیر ممالک کے ساتھ ساتھ ترقی یافتہ ممالک میں بھی کینسر کا ایک سبب سبزیوں اور پھلوں کا کم تر ہوتا استعمال ہے اور عموما لوگ سبزیوں اور پھلوں کے استعمال کو نظر انداز کرتے ہیں جو صحت کی خرابی کی ایک اہم وجہ ہے ۔
اس حوالے سے ڈوئچے ویلے سے بات کرتے ہوئے شوکت خانم میموریل کیسنر ہسپتال اور تحقیقی مرکز کے وابستہ ڈاکٹر نتاشہ انور کا کہنا تھا کہ موجودہ دور میں تیز رفتار زندگی نے انسانی خوراک پر انتہائی منفی اثرات ڈالے ہیں اور لوگ خوراک کے معاملے میں ڈبہ بند خوراک پر انحصار کرنے لگے ہیں ۔
جس کے باعث زیادہ عرصے تک محفوظ رہنے والی خوراک استعمال کی جارہی ہے جس میں موجود کیمیکلز انسانی صحت پر منفی اثرات مرتب کر رہے ہیں ۔
ڈاکٹر نتاشا انور کا کہنا تھا کہ ایسی خوراک فطری خوراک کا نعم البدل ہر گز نہیں ہو سکتی ۔
سبزیوں اور پھلوں کی کینسر کے خلاف مزاحمت کے حوالے سے مسلسل تحقیق چل رہی ہے اور آئے روز اس حوالے سے تحقیقاتی رپورٹس سامنے آ رہی ہیں ابھی حال ہی میں امریکی طبی ماہرین نے کہا ہے کہ سرطان کے خاتمے کیلئے انگوروں کے بیجوں کا گودا نہایت کارآمد ثابت ہوا ہے ۔
طبی ماہرین نے لیبارٹری میں تجربات کرتے ہوئے خون کے سرطان پر انگوروں کے بیجوں کے گودے کو آزمایا اور صرف24 گھنٹوں میں سرطان کے خلیوں کی 76 فیصد تعداد کو کم ہوتے دیکھا جبکہ خون کے اندر صحت مند خلیے اس سے محفوظ رہے ۔
طبی ماہرین نے ان تجربات کے بعد امید ظاہر کی ہے کہ عالمی سطح پر اب خون کے سرطان کے علاج کی نئی دوا تیار کرنے میں مدد ملے گی ۔
اس سے قبل ’’ لاکومیا ‘‘ کے مریضوں کو کثرت سے انگور کھانے کی سفارش کی جاتی تھی جس کو بنیاد بناکر نئی تحقیق شروع کی گئی تھی ۔
طبی ماہرین نے کہا ہے کہ انگوروں کے بیجوں میں جسم سے فاسد مادے خارج کرنے کی بھرپور صلاحیت ہے اور دل کو مضبوط بنانے کیلئے یہ ایک بہترین ٹانک ثابت ہوتے ہیں ۔
ماہرین نے مزید کہا ہے کہ ان بیجوں میں جلد ، چھاتی ، مثانہ ، پھیپھڑوں اور معدے کے سرطان کے خلاف بھی قوت دیکھی گئی ہے ۔
چوہوں میں چھاتی اور جلد کے کینسر ٹیومر کا سائز ان بیجوں کے استعمال سے کم ہوگیا تھا ۔
یہ تحقیق یونیورسٹی آف کینٹیکی کے پروفیسر زینگ لینگ شائی نے مکمل کی ہے ۔ 
"""

# summarizer = AmjadSummarizer(text)
# print(text)
# s = summarizer.summarize()
# print(s)
