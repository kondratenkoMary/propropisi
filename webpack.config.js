const path = require('path');
const fs = require('fs');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const SVGSpritemapPlugin = require('svg-spritemap-webpack-plugin');
const postcssPresetEnv = require('postcss-preset-env');
const postcssDiscardDuplicated = require('postcss-discard-duplicates');
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

const NODE_ENV = process.env.NODE_ENV;
const isDevelopment = NODE_ENV === 'development';
const JS_REGEX = /\.js$|\.es6$|\.babel$/;
const EXCLUDE_REGEX = /node_modules/;

const getPath = (folderName) => path.join(__dirname, folderName);

let jsonConfig = {};
try {
    jsonConfig = require('./config.json');
} catch (e) {
    jsonConfig = require('./config.test.json');
}

// write static url const for LESS
fs.writeFileSync(path.join(__dirname, 'assets', 'app', 'front', 'static-url.less'), '@static_url: \'' + (jsonConfig.HOT_RELOADING ? jsonConfig.STATIC_URL_HOT : jsonConfig.STATIC_URL) + '\';\n');

module.exports = {

    devtool: isDevelopment ? 'cheap-module-source-map' : 'sourcemap',

    mode: isDevelopment ? 'development' : 'production',

    entry: {
        main: getPath('./assets/app/front/App'),
        login: getPath('./assets/app/front/Login')
    },

    output: {
        filename: isDevelopment ? 'app/front/[name].js' : 'app/[name]/main.[hash].js',
        chunkFilename: isDevelopment ? 'app/front/[name].chunk.js' : 'app/front/[name].chunk.[hash].js',
        path: path.join(__dirname, 'static'),
        publicPath: jsonConfig.HOT_RELOADING ? 'http://127.0.0.1:9999/static/' : '/static/'
    },

    optimization: {
        splitChunks: {
            chunks: 'all',
            cacheGroups: {
                default: false,
                vendors: false
            }
        },
        minimize: !isDevelopment,
        minimizer: [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})]
    },

    resolve: {
        modules: [
            'node_modules',
            getPath('/assets/app/'),
            getPath('/assets/favicon/'),
            getPath('/assets/js/django_js_front/'),
            getPath('/assets/js/')
        ]
    },

    resolveLoader: {
        modules: [getPath('node_modules')]
    },

    devServer: {
        historyApiFallback: true,
        noInfo: false,
        headers: {
            'Access-Control-Allow-Origin': '\*'
        },
        contentBase: false,
        clientLogLevel: 'warning',
        port: 9999,
        hot: true
    },

    module: {
        rules: [
            {
                test: JS_REGEX,
                exclude: [
                    EXCLUDE_REGEX,
                    path.join(__dirname, 'assets/js')
                ],
                enforce: 'pre',
                use: [
                    {
                        loader: 'eslint-loader',
                        options: {
                            cache: false,
                            fix: isDevelopment
                        }
                    }
                ]
            },
            {
                test: JS_REGEX,
                exclude: [EXCLUDE_REGEX, path.join(__dirname, 'assets/js')],
                use: [{
                    loader: 'babel-loader'
                }]
            },
            {
                test: /reverse\.js$/,
                use: ['imports-loader?me=>{}', 'exports-loader?me.Urls']
            },
            {
                test: /\.jinja$/,
                use: {
                    loader: 'nunjucks-loader',
                    options: {
                        config: __dirname + '/nunjucks.config.js'
                    }
                }
            },
            {
                test: /\.less$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    }, {
                        loader: 'css-loader',
                        options: {
                            url: false
                        }
                    }, {
                        loader: 'postcss-loader',
                        options: {
                            plugins() {
                                return [
                                    postcssPresetEnv(),
                                    postcssDiscardDuplicated()
                                ];
                            }
                        }
                    }, {
                        loader: 'less-loader'
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    }, {
                        loader: 'css-loader'
                    }, {
                        loader: 'postcss-loader',
                        options: {
                            plugins() {
                                return [
                                    postcssPresetEnv()
                                ];
                            }
                        }
                    }
                ]
            }
        ]
    },

    plugins: [
        new CleanWebpackPlugin({
            cleanOnceBeforeBuildPatterns: [
                'app/**'
            ],
            cleanStaleWebpackAssets: false

        }),
        new CopyWebpackPlugin([
            {from: getPath('assets/fonts'), to: 'fonts/'},
            {from: getPath('assets/img'), to: 'img/'},
            {from: getPath('assets/svg'), to: 'svg/'},
            {from: getPath('assets/favicon'), to: 'favicon/'}
        ]),
        new MiniCssExtractPlugin({
            filename: isDevelopment ? 'app/front/[name].css' : 'app/[name]/[name].[hash].css',
            chunkFilename: isDevelopment ? 'app/front/[name].chunk.css' : 'app/front/[name].chunk.[hash].css'
        }),
        new webpack.DefinePlugin({
            'process.env': {
                isStaging: (NODE_ENV === 'development' || NODE_ENV === 'staging'),
                NODE_ENV: `"${NODE_ENV}"`
            }
        }),
        new SVGSpritemapPlugin(getPath('assets/svg/front/*.svg'), {
            output: {
                filename: 'svg/front/sprite.symbol.svg',
                svg4everybody: false,
                svgo: true
            },
            sprite: {
                prefix: false,
                generate: {
                    use: true
                }
            }
        }),
        new BundleTracker({filename: './webpack.stats.json'})
    ],

    externals: {
        jquery: 'jQuery'
    },

    performance: {
        hints: false
    },

    stats: {
        colors: true,
        hash: false,
        version: false,
        timings: false,
        assets: false,
        chunks: true,
        modules: false,
        reasons: false,
        children: false,
        source: false,
        warnings: true,
        publicPath: false
    }
};
