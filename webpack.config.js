const path = require('path')
const { VueLoaderPlugin } = require('vue-loader')
//const ExtractTextPlugin = require('extract-text-webpack-plugin')
var MiniCssExtractPlugin = require('mini-css-extract-plugin')

//const isProduction = process.env.NODE_ENV === 'production'

module.exports = {
  mode: 'production',

  entry: './src/index.js',

  output: {
  // 出力するファイル名
    filename: 'bundle.js',
    // 出力先のパス（絶対パスを指定する必要がある）
    path: path.join(__dirname, 'src')
  },

  module: {
    rules: [
      {
        test: /\.vue$/,
        exclude: /node_modules/,
        loader: 'vue-loader',
        options: {
          //extractCSS: isProduction,
          loaders: {
            scss: "vue-style-loader"
          }
        }
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader"
      },
      {
         test: /\.css$/,
         use: [
           process.env.NODE_ENV !== 'production'
             ? 'vue-style-loader'
             : MiniCssExtractPlugin.loader,
           'css-loader'
         ]
       },
       {
         test: /\.(jpg|png)$/,
         loaders: 'url-loader'
       },
       {
          test: /\.s(c|a)ss$/,
          use: [
            'vue-style-loader',
            'css-loader',
            {
              loader: 'sass-loader',
              options: {
                implementation: require('sass'),
                fiber: require('fibers'),
                indentedSyntax: true // optional
              }
            }
          ]
        }
       /*{
          test: /\.(gif|png|jpe?g|svg)$/i,
          use: [
             'file-loader',
            {
              loader: 'image-webpack-loader',
              options: {
                webp: {
                  quality: 80
                }
              }
            }
          ]
        }*/
    ]

  },
  plugins: [
    new VueLoaderPlugin(),
    new MiniCssExtractPlugin({filename: 'style.css'})
    //new ExtractTextPlugin({ filename: 'common.[chunkhash].css' })
  ]
}
