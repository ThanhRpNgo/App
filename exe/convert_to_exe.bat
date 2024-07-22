pyinstaller ^
    --clean ^
    --onefile ^
    --noconsole ^
    --icon "imgs/grade.ico" ^
    "../main.py" ^
    "../parameter.py" ^
    "../tklib.py" ^
    "../modules/window_first.py" ^
    "../modules/window_note.py" ^
    "../modules/window_second.py"
    "../modules/window_waiting.py" ^
    "../MCQs/OMR_checker.py" ^
    "../MCQs/OMR_CheckTest.py" ^
    "../MCQs/system.py" ^
    "../MCQs/Src/check_code_and_answer.py" ^
    "../MCQs/Src/findBlackRect.py" ^
    "../MCQs/Src/findFrame.py" ^
    "../MCQs/Src/inforFunc.py" ^
    "../MCQs/Src/template_excel.py" ^
    "../MCQs/Src/utlis.py"
