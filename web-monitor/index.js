
/**
 * 收集一些用户特征
 */
function report() {

    const domain = document.domain || ''

    const title = document.title || ''

    const referrer = document.referrer || ''

    const screenWidth = window.screen.width || 0
    const screenHeight = window.screen.height || 0

    const lang = navigator.language || ''

    const ua = navigator.userAgent

    const loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart || 0

    const time = new Date()

}