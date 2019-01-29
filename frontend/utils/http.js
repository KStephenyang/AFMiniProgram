import { config } from "../config.js"

class HTTP {
    request({ url, data = {}, method = 'GET' }) {
        console.log(url, data, method)
        return new Promise((resolve, reject) => {
            this._request(url, resolve, reject, data, method)
        })
    }
    _request(url, resolve, reject, data, method) {
        wx.request({
            url: "http://127.0.0.1:8000/" + url,
            method: method,
            data: data,
            header: {
                "content-type": "application/json"
            },
            success: (res) => {
                console.log('suc:res=', res)
                resolve(res.data)
            },
            fail:(err) =>{
                console.log('fail:err=', err)
                reject()
                this._show_error()
            }
        })
    }
    _show_error(){
        wx.showToast({
            title:"发生一个错误",
            icon:"none",
            duration:2000
        })
    }
}
export { HTTP }