var reserveFlag = true;
var getUrl = function () {
    return "http://61.76.4.67:9082/";
}

var url_list = {
    "Login": getUrl() + "EzlibSeat.asmx/LoginJ?callback=''",
    "GetUser": getUrl() + "EzlibSeat.asmx/GetUserJ?callback=''",
    "DoSeatSelect": getUrl() + "EzlibSeat.asmx/DoSeatSelectJ?callback=''",
    "DoReturn": getUrl() + "EzlibSeat.asmx/DoReturnJ?callback=''",
    "DoReserveCancel": getUrl() + "EzlibSeat.asmx/DoReserveCancelJ?callback=''",
    "DoReserve": getUrl() + "EzlibSeat.asmx/DoReserveJ?callback=''",
    "DoExtend": getUrl() + "EzlibSeat.asmx/DoExtendJ?callback=''",
    "DoCancel": getUrl() + "EzlibSeat.asmx/DoCancelJ?callback=''"
};
