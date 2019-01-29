const NAV_DICT = {
    "设备":"device",
    "收藏":"favorate",
    "目标":"goal",
    "商城":"mall"
}

const promisic = function(func){
    return function(params={}){
        return new Promise((resolve, reject) => {
            const args = Object.assign(params, {
                success:res=>{
                    resolve(res)
                },
                fail:error=>{
                    reject(error)
                }
            })
            func(args)
        })
    }
}

export {promisic, NAV_DICT}