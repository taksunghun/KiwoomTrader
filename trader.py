from core import KWCore
from constants import KWErrorCode

from importer import *

class KWTrader(KWCore):

    def initialize(self):
        self.tr_list['opt10001'] = Opt10001(self)
        self.tr_list['opt10002'] = Opt10002(self)
        self.tr_list['opt10003'] = Opt10003(self)
        self.tr_list['opt10004'] = Opt10004(self)
        self.tr_list['opt10005'] = Opt10005(self)
        self.tr_list['opt10006'] = Opt10006(self)
        self.tr_list['opt10007'] = Opt10007(self)
        self.tr_list['opt10008'] = Opt10008(self)
        self.tr_list['opt10009'] = Opt10009(self)
        self.tr_list['opt10010'] = Opt10010(self)
        # self.tr_list['opt10011'] = Opt10011(self)     # opt10011 : Does not exist.
        self.tr_list['opt10012'] = Opt10012(self)
        self.tr_list['opt10013'] = Opt10013(self)
        self.tr_list['opt10014'] = Opt10014(self)
        self.tr_list['opt10015'] = Opt10015(self)
        self.tr_list['opt10016'] = Opt10016(self)
        self.tr_list['opt10017'] = Opt10017(self)
        self.tr_list['opt10018'] = Opt10018(self)
        self.tr_list['opt10019'] = Opt10019(self)
        self.tr_list['opt10020'] = Opt10020(self)
        self.tr_list['opt10021'] = Opt10021(self)
        self.tr_list['opt10022'] = Opt10022(self)
        self.tr_list['opt10023'] = Opt10023(self)
        self.tr_list['opt10024'] = Opt10024(self)
        self.tr_list['opt10025'] = Opt10025(self)
        self.tr_list['opt10026'] = Opt10026(self)
        self.tr_list['opt10027'] = Opt10027(self)
        self.tr_list['opt10028'] = Opt10028(self)
        self.tr_list['opt10029'] = Opt10029(self)
        self.tr_list['opt10030'] = Opt10030(self)
        self.tr_list['opt10031'] = Opt10031(self)
        self.tr_list['opt10032'] = Opt10032(self)
        self.tr_list['opt10033'] = Opt10033(self)
        self.tr_list['opt10034'] = Opt10034(self)
        self.tr_list['opt10035'] = Opt10035(self)
        self.tr_list['opt10036'] = Opt10036(self)
        self.tr_list['opt10037'] = Opt10037(self)
        self.tr_list['opt10038'] = Opt10038(self)
        self.tr_list['opt10039'] = Opt10039(self)
        self.tr_list['opt10040'] = Opt10040(self)
        self.tr_list['opt10041'] = Opt10041(self)
        self.tr_list['opt10042'] = Opt10042(self)
        self.tr_list['opt10043'] = Opt10043(self)
        self.tr_list['opt10044'] = Opt10044(self)
        self.tr_list['opt10045'] = Opt10045(self)
        self.tr_list['opt10046'] = Opt10046(self)
        self.tr_list['opt10047'] = Opt10047(self)
        self.tr_list['opt10048'] = Opt10048(self)
        self.tr_list['opt10049'] = Opt10049(self)
        self.tr_list['opt10050'] = Opt10050(self)
        self.tr_list['opt10051'] = Opt10051(self)
        self.tr_list['opt10052'] = Opt10052(self)
        self.tr_list['opt10053'] = Opt10053(self)
        # self.tr_list['opt10054'] = Opt10054(self)     # opt10054 : Does not exist.
        self.tr_list['opt10055'] = Opt10055(self)
        # self.tr_list['opt10056'] = Opt10056(self)     # opt10056 : Does not exist.
        # self.tr_list['opt10057'] = Opt10057(self)     # opt10057 : Does not exist.
        self.tr_list['opt10058'] = Opt10058(self)
        self.tr_list['opt10059'] = Opt10059(self)
        self.tr_list['opt10060'] = Opt10060(self)
        self.tr_list['opt10061'] = Opt10061(self)
        self.tr_list['opt10062'] = Opt10062(self)
        self.tr_list['opt10063'] = Opt10063(self)
        self.tr_list['opt10064'] = Opt10064(self)
        self.tr_list['opt10065'] = Opt10065(self)


    def connection(self):
        self.comm_connect()


    # [ opt10001 : 주식기본정보요청 ]
    def opt10001(self, code, prev_next, screen_no):
        return self.tr_list['opt10001'].tr_opt(code, prev_next, screen_no)


    #  [ opt10002 : 주식거래원요청 ]
    def opt10002(self, code, prev_next, screen_no):
        return self.tr_list['opt10002'].tr_opt(code, prev_next, screen_no)


    #  [ opt10003 : 체결정보요청 ]
    def opt10003(self, code, prev_next, screen_no):
        return self.tr_list['opt10003'].tr_opt(code, prev_next, screen_no)


    # [ opt10004 : 주식호가요청 ]
    def opt10004(self, code, prev_next, screen_no):
        return self.tr_list['opt10004'].tr_opt(code, prev_next, screen_no)


    # [ opt10005 : 주식일주월시분요청 ]
    def opt10005(self, code, prev_next, screen_no):
        return self.tr_list['opt10005'].tr_opt(code, prev_next, screen_no)


    # [ OPT10006 : 주식시분요청 ]
    def opt10006(self, code, prev_next, screen_no):
        return self.tr_list['opt10006'].tr_opt(code, prev_next, screen_no)


    # [ opt10007 : 시세표성정보요청 ]
    def opt10007(self, code, prev_next, screen_no):
        return self.tr_list['opt10007'].tr_opt(code, prev_next, screen_no)


    # [ opt10008 : 시세표성정보요청 ]
    def opt10008(self, code, prev_next, screen_no):
        return self.tr_list['opt10008'].tr_opt(code, prev_next, screen_no)


    # [ OPT10009 : 주식기관요청 ]
    def opt10009(self, code, prev_next, screen_no):
        return self.tr_list['opt10009'].tr_opt(code, prev_next, screen_no)


    # [ OPT10010 : 업종프로그램요청 ]
    def opt10010(self, code, prev_next, screen_no):
        return self.tr_list['opt10010'].tr_opt(code, prev_next, screen_no)


    # [ opt10012 : 주문체결요청 ]
    def opt10012(self, code, prev_next, screen_no):
        return self.tr_list['opt10012'].tr_opt(code, prev_next, screen_no)


    # [ opt10013 : 신용매매동향요청 ]
    def opt10013(self, code, date, type_flag, prev_next, screen_no):
        return self.tr_list['opt10013'].tr_opt(code, date, type_flag, prev_next, screen_no)


    # [ opt10014 : 공매도추이요청 ]
    def opt10014(self, code, date_type, date_from, date_to, prev_next, screen_no):
        return self.tr_list['opt10014'].tr_opt(code, date_type, date_from, date_to, prev_next, screen_no)


    # [ opt10015 : 일별거래상세요청 ]
    def opt10015(self, code, date, prev_next, screen_no):
        return self.tr_list['opt10015'].tr_opt(code, date, prev_next, screen_no)


    # [ OPT10016 : 신고저가요청 ]
    def opt10016(self, market_type, input1, input2, input3, input4, input5, input6, date, prev_next, screen_no):
        return self.tr_list['opt10016'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, date, prev_next, screen_no)


    # [ opt10017 : 상하한가요청 ]
    def opt10017(self, market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10017'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ OPT10018 : 고저가근접요청 ]
    def opt10018(self, input0, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10018'].tr_opt(input0, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ opt10019 : 가격급등락요청 ]
    def opt10019(self, market_type, input1, date_type, date, input4, input5, input6, input7, input8, prev_next, screen_no):
        return self.tr_list['opt10019'].tr_opt(market_type, input1, date_type, date, input4, input5, input6, input7, input8, prev_next, screen_no)


    # [ OPT10020 : 호가잔량상위요청 ]
    def opt10020(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10020'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10021 : 호가잔량급증요청 ]
    def opt10021(self, market_type, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10021'].tr_opt(market_type, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ OPT10022 : 잔량율급증요청 ]
    def opt10022(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10022'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10023 : 거래량급증요청 ]
    def opt10023(self, market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10023'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ OPT10024 : 거래량갱신요청 ]
    def opt10024(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10024'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10025 : 매물대집중요청 ]
    def opt10025(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10025'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ opt10026 : 고저PER요청 ]
    def opt10026(self, per_type, prev_next, screen_no):
        return self.tr_list['opt10026'].tr_opt(per_type, prev_next, screen_no)


    # [ opt10027 : 전일대비등락률상위요청 ]
    def opt10027(self, market_type, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10027'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ opt10028 : 시가대비등락률요청 ]
    def opt10028(self, input0, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10028'].tr_opt(input0, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ OPT10029 : 예상체결등락률상위요청 ]
    def opt10029(self, market_type, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10029'].tr_opt(market_type, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ OPT10030 : 당일거래량상위요청 ]
    def opt10030(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10030'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10031 : 전일거래량상위요청 ]
    def opt10031(self, market_type, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10031'].tr_opt(market_type, input1, input2, input3, prev_next, screen_no)


    # [ OPT10032 : 거래대금상위요청 ]
    def opt10032(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt10032'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt10033 : 신용비율상위요청 ]
    def opt10033(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10033'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10034 : 외인기간별매매상위요청 ]
    def opt10034(self,  market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10034'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10035 : 외인연속순매매상위요청 ]
    def opt10035(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10035'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10036 : 매매상위요청 ]
    def opt10036(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt10036'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt10037 : 외국계창구매매상위요청 ]
    def opt10037(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10037'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ opt10038 : 종목별증권사순위요청 ]
    def opt10038(self, code, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10038'].tr_opt(code, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10039 : 증권사별매매상위요청 ]
    def opt10039(self, input0, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10039'].tr_opt(input0, input1, input2, input3, prev_next, screen_no)


    # [ opt10040 : 당일주요거래원요청 ]
    def opt10040(self, code, prev_next, screen_no):
        return self.tr_list['opt10040'].tr_opt(code, prev_next, screen_no)


    # [ opt10041 : 조기종료통화단위요청 ]
    def opt10041(self, code, input1, prev_next, screen_no):
        return self.tr_list['opt10041'].tr_opt(code, input1, prev_next, screen_no)


    # [ opt10042 : 순매수거래원순위요청 ]
    def opt10042(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10042'].tr_opt(code, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ opt10043 : 거래원매물대분석요청 ]
    def opt10043(self, code, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10043'].tr_opt(code, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ OPT10044 : 일별기관매매종목요청 ]
    def opt10044(self, input0, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10044'].tr_opt(input0, input1, input2, input3, prev_next, screen_no)


    # [ opt10045 : 종목별기관매매추이요청 ]
    def opt10045(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10045'].tr_opt(code, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ opt10046 : 체결강도추이시간별요청 ]
    def opt10046(self, code, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10046'].tr_opt(code, input1, input2, prev_next, screen_no)


    # [ opt10047 : 체결강도추이일별요청 ]
    def opt10047(self, code, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10047'].tr_opt(code, input1, input2, prev_next, screen_no)


    # [ OPT10048 : ELW일별민감도지표요청 ]
    def opt10048(self, code, prev_next, screen_no):
        return self.tr_list['opt10048'].tr_opt(code, prev_next, screen_no)


    # [ OPT10049 : ELW투자지표요청 ]
    def opt10049(self, input0, input1, code, prev_next, screen_no):
        return self.tr_list['opt10049'].tr_opt(input0, input1, code, prev_next, screen_no)


    # [ OPT10050 : ELW민감도지표요청 ]
    def opt10050(self, code, prev_next, screen_no):
        return self.tr_list['opt10050'].tr_opt(code, prev_next, screen_no)


    # [ OPT10051 : 업종별투자자순매수요청 ]
    def opt10051(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10051'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ opt10052 : 거래원순간거래량요청 ]
    def opt10052(self, input0, code, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10052'].tr_opt(input0, code, input2, input3, input4, prev_next, screen_no)


    # [ opt10053 : 당일상위이탈원요청 ]
    def opt10053(self, code, prev_next, screen_no):
        return self.tr_list['opt10053'].tr_opt(code, prev_next, screen_no)


    # [ opt10055 : 당일전일체결대량요청 ]
    def opt10055(self, code, input1, prev_next, screen_no):
        return self.tr_list['opt10055'].tr_opt(code, input1, prev_next, screen_no)


    # [ OPT10058 : 투자자별일별매매종목요청 ]
    def opt10058(self, from_date, to_date, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10058'].tr_opt(from_date, to_date, input2, input3, input4, prev_next, screen_no)


    # [ opt10059 : 종목별투자자기관별요청 ]
    def opt10059(self, date, code, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10059'].tr_opt(date, code, input2, input3, input4, prev_next, screen_no)


    # [ opt10060 : 종목별투자자기관별차트요청 ]
    def opt10060(self, date, code, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10060'].tr_opt(date, code, input2, input3, input4, prev_next, screen_no)


    # [ opt10061 : 종목별투자자기관별합계요청 ]
    def opt10061(self, code, date_from, date_to, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10061'].tr_opt(code, date_from, date_to, input3, input4, input5, prev_next, screen_no)


    # [ opt10062 : 동일순매매순위요청 ]
    def opt10062(self, date_from, date_to, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10062'].tr_opt(date_from, date_to, input2, input3, input4, input5, prev_next, screen_no)


    # [ opt10063 : 장중투자자별매매요청 ]
    def opt10063(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10063'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ opt10064 : 장중투자자별매매차트요청 ]
    def opt10064(self, market_type, input1, input2, code, prev_next, screen_no):
        return self.tr_list['opt10064'].tr_opt(market_type, input1, input2, code, prev_next, screen_no)


    # [ OPT10065 : 장중투자자별매매상위요청 ]
    def opt10065(self, input0, market_type, input2, prev_next, screen_no):
        return self.tr_list['opt10065'].tr_opt(input0, market_type, input2, prev_next, screen_no)
