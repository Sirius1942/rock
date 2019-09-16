import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
import store from '@/store'
import { getToken } from '@/utils/auth'

// create an axios instance
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(
  config => {
    console.log('in if 1')
    // 后台使用jwt时候发送post请求必须使用 formdata模式
    if (config.method === 'post') {
      // JSON 转换为 FormData
      if (config.data) {
        console.log('in if 2')
        const formData = new FormData()
        Object.keys(config.data).forEach(key => formData.append(key, config.data[key]))
        config.data = formData
      }
    }
    if (store.getters.token) {
      // let each request carry token
      // ['X-Token'] is a custom headers key
      // please modify it according to the actual situation
      // config.headers['X-Token'] = getToken()
      config.headers.Authorization = getToken()
    }
    config.headers['Content-Type'] = 'application/json'
    return config
  },
  error => {
    // do something with request error
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

// // response interceptor
// service.interceptors.response.use(
//   // res => {
//   //   // 对响应数据做些事
//   //   if (!res.data.status === 200) {
//   //     alert(res.error_msg)
//   //     return Promise.reject(res)
//   //   }
//   //   console.log('in return') // for debug
//   //   console.log(res) // for debug
//   //   return res
//   // }, error => {
//   //   if (error.response.status === 401) {
//   //     // 401 说明 token 验证失败
//   //     // 可以直接跳转到登录页面，重新登录获取 token
//   //     // location.href = '/login'
//   //   } else if (error.response.status === 500) {
//   //     // 服务器错误
//   //     // do something
//   //     return Promise.reject(error.response.data)
//   //   }
//   //   // 返回 response 里的错误信息
//   //   return Promise.reject(error.response.data)
//   // }
//   // }
//   /**
//    * If you want to get http information such as headers or status
//    * Please return  response => response
//   */

//   /**
//    * Determine the request status by custom code
//    * Here is just an example
//    * You can also judge the status by HTTP Status Code
//    */
//   response => {
//     console.log('in response')
//     const res = response.data
//     console.log(res)
//     // if(res.access){

//     // }
//     return res
//   // if the custom code is not 20000, it is judged as an error.xian
//   if (res.code !== 20000) {
//     Message({
//       message: res.message || 'Error',
//       type: 'error',
//       duration: 5 * 1000
//     })

//     // 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
//     if (res.code === 50008 || res.code === 50012 || res.code === 50014) {
//       // to re-login
//       MessageBox.confirm('You have been logged out, you can cancel to stay on this page, or log in again', 'Confirm logout', {
//         confirmButtonText: 'Re-Login',
//         cancelButtonText: 'Cancel',
//         type: 'warning'
//       }).then(() => {
//         store.dispatch('user/resetToken').then(() => {
//           location.reload()
//         })
//       })
//     }
//     return Promise.reject(new Error(res.message || 'Error'))
//   } else {
//     return res
//   }
//   },
//   error => {
//     console.log('err' + error) // for debug
//     Message({
//       message: error.message,
//       type: 'error',
//       duration: 5 * 1000
//     })
//     return Promise.reject(error)
//   }
// )
// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
  */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  response => {
    console.log('in response')
    const res = response.data
    console.log(res)
    // if the custom code is not 20000, it is judged as an error.
    if (res.code !== 20000) {
      Message({
        message: res.message || 'error',
        type: 'error',
        duration: 5 * 1000
      })
      // 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
      if (res.code === 50008 || res.code === 50012 || res.code === 50014) {
        // to re-login
        MessageBox.confirm('You have been logged out, you can cancel to stay on this page, or log in again', 'Confirm logout', {
          confirmButtonText: 'Re-Login',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(() => {
          store.dispatch('user/resetToken').then(() => {
            location.reload()
          })
        })
      }
      return Promise.reject(res.message || 'error')
    } else {
      return res
    }
  },
  error => {
    console.log('err' + error) // for debug
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

export default service
