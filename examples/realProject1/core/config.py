# Github: GWillS163
# User: 駿清清 
# Date: 17/10/2022 
# Time: 17:38

surveyExlPh = r"" \
              r"D:\work\考核RPA_Exl\Input\2022-11-28_正式\团建表格输入配置表_2022-11-3.xlsx"
peopleAnsExlPh = r"D:\work\考核RPA_Exl\Input\2022-11-28_正式\2022年度团建工作成效调研问卷-群众 .xlsx"
groupAnsExlPh = r"D:\work\考核RPA_Exl\Input\2022-11-28_正式\2022年度团建工作成效调研问卷-团员 .xlsx"

savePath = r"D:\work\考核RPA_Exl\Output"
fileYear = ""
fileName = "GroupBuild"
surveyTestShtName = "测试问卷"
sht1ModuleName = "调研结果_输出模板"
sht2ModuleName = "调研成绩_输出模板"
sht3ModuleName = "调研结果（2022年）_输出模板"
sht4ModuleName = "调研成绩（2022年）_输出模板"
sht1Name = "调研结果"
sht2Name = "调研成绩"
sht3Name = "调研结果（2022年）"
sht4Name = "调研成绩（2022年）"

# Sheet1 生成配置 : F, G
# sht1IndexScpFromSht0, sht1TitleCopyFromSttCol, sht1TitleCopyToSttCol = ["A1:F31", "F", "G"]
sht1IndexScpFromSht0 = "A1:F31"
sht1TitleCopyFromSttCol = "F"
sht1TitleCopyToSttCol = "G"
# Sheet2 生成配置: "C1:J1", "D"
# sht2DeleteCopiedColScp, sht2MdlTltStt = ["C1:J1", "D"]
sht2DeleteCopiedColScp = "C1:J1"
sht2MdlTltStt = "D"
# Sheet3 生成配置:  "L", "J", "K"
# sht3MdlTltStt, sht3SurLastCol, sht3ResTltStt = ["L", "J", "K"]
sht3MdlTltStt = "L"
sht3SurLastCol = "J"
sht3ResTltStt = "K"

# Sheet4 生成配置:
# sht4IndexFromMdl4Scp, sht4TitleFromSht2Scp, sht4SumTitleFromMdlScp = ['A4:B52', 'A1:C17', "P1:Q3"]
sht4IndexFromMdl4Scp = 'A4:B52'
sht4TitleFromSht2Scp = 'A1:C17'
sht4SumTitleFromMdlScp = "P1:Q3"

sht1WithLv = {'平台生态部': {'团建与综合管理室': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0], '二级单位': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0]}, '重要客户中心': {'团建与综合管理室': [8.0, 9.0, 9.0, 9.0, 9.0, 10.0, 8.0, 8.0, 10.0, 10.0, 10.0, 9.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 9.0, 10.0, 9.0, 9.0, 0.0, 10.0, 9.0, 10.0, 9.0, 9.0], '二级单位': [8.0, 9.0, 9.0, 9.0, 9.0, 10.0, 8.0, 8.0, 10.0, 10.0, 10.0, 9.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 9.0, 10.0, 9.0, 9.0, 0.0, 10.0, 9.0, 10.0, 9.0]}, '网络与信息安全中心': {'信安室': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 6.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0], '二级单位': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 6.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0]}, '北京融昱信息技术有限公司': {'团建与综合管理室': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 9.0, 10.0, 10.0], '二级单位': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 9.0, 10.0]}, '信息系统部': {'团建与综合管理室': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 9.0, 10.0, 10.0], '二级单位': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 10.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 9.0, 10.0]}, '行政服务中心': {'团建与综合管理室': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 6.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 9.0, 10.0, 10.0], '二级单位': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, -1.0, 10.0, 6.0, 0.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.0, 10.0, 10.0, 9.0, 10.0]}}


