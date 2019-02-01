// pages/user-info/user-info.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    my_info: {
      my_name: '请输入头马昵称',
      my_level: '请输入头马等级',
      my_role: '请输入头马角色',
      my_duty: '请输入头马职责',
      my_mentor: '请输入头马导师',
      my_club: '请输入头马名称'
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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

  },

  onNavigateToMy: function (event) {
    wx.switchTab({
      url: '/pages/my/my',
    })
  }
})
