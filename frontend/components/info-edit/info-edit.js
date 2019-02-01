// components/info-edit/info-edit.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    item: {
      type: String
    },
    placeholder_text: {
      type: String
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    item_value: ''
  },

  /**
   * 组件的方法列表
   */
  methods: {
    /**
    * 监听文本框输入，并把输入的值保存在data变量中
    */
    listenerItemInput: function (e) {
      console.log(this.item + ":" + e.detail.value)
      this.data.item_value = e.detail.value;
    },
  }
})
