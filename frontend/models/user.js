import { HTTP } from '../utils/http'

class UserModel extends HTTP {
    getOpenId(code) {
        return this.request({
            url:"user/code/",
            data:code
        })
    }

    getUserBaseinfo(){
        return this.request({
            url:"user/baseinfo/",
        })
    }

    postUserBaseinfo(userBaseinfo){
        return this.request({
            url:"user/baseinfo/",
            data:userBaseinfo,
            method:'POST'
        })
    }

    getUserInteract(){
        return this.request({
            url:"user/interact/"
        })
    }


}

export {UserModel}