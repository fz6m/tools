function hexToRGB(hex) {
    const hexx = hex.replace('#', '0x')
    const r = hexx >> 16
    const g = hexx >> 8 & 0xff
    const b = hexx & 0xff
    return `rgb(${r}, ${g}, ${b})`
}
