import View
import Model


def start():
    choice = View.InputChoice()
    if choice == 1:
        a = View.InputData('первое')
        Model.set_first(a)
        while True:
            oper = View.InputOperator()
            if oper == '=':
                break
            b = View.InputData('второе')
            Model.set_second(b)
            Model.set_result(oper)
            result = Model.get_result()
            if result == None:
                View.division_by_zero()
                break
            first = Model.get_first()
            second = Model.get_second()
            View.OutputResult(first, second, oper, result)
            # View.print_window(result)
            Model.set_first(result)
    elif choice == 2:
        oString = View.InputString()
        Model.Set_Ostring(oString)
        result = Model.Set_parserString()
        # View.print_window(result)
        View.PrintResultString(oString, result)
