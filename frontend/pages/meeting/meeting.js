// pages/news/news.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    selected: [
      {
        date: '2018-5-21'
      }, {
        date: '2018-5-22'
      }, {
        date: '2018-5-24'
      }, {
        date: '2018-5-25'
      }
    ],
    book_info:{
      'club': 'AmazingFridayTMC',
      'meeting_time': '2019-01-25 19:00',
      'TME': 'Kelly',
      'TTM': '点击预定',
      'GE': '点击预定',
      'Timer': '点击预定',
      'Ah_counter': '点击预定',
      'Grammarian': 'Kelly',
      'Speech1': 'Stephen',
      'Speech2': '点击预定',
      'Speech3': 'Jack',
      'IE1': 'Johnson',
      'IE2': '点击预定',
      'IE3': 'Kelly',
      'SAA': 'Curry',
      'Recorder': '点击预定',
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
  * 日历是否被打开
  */
  bindselect(e) {
    console.log(e.detail.ischeck)
  },

  /**
   * 获取选择日期
   */
  bindgetdate(e) {
    let time = e.detail;
    console.log(time)

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})