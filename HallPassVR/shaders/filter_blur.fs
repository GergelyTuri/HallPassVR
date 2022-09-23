/////SHIFT RGB FILTER/////
//www.cloneproduction.net
#include std_head_fs.inc

varying vec2 uv;

#define factor 0.04

void main(void){
  float spread = unif[16][0];
  vec2 f = uv * spread;
  float minc = 1.0;
  float maxc = 0.0;
  float l;

  vec4 c = texture2D(tex0, uv);
  
  c += texture2D(tex0, uv + vec2(-1.0, 0.0) * f);
  c += texture2D(tex0, uv + vec2(-1.414, 1.414) * f);
  c += texture2D(tex0, uv + vec2(0.0, 1.0) * f);
  c += texture2D(tex0, uv + vec2(1.414, 1.414) * f);
  c += texture2D(tex0, uv + vec2(1.0, 0.0) * f);
  c += texture2D(tex0, uv + vec2(1.414, -1.414) * f);
  c += texture2D(tex0, uv + vec2(0.0, -1.0) * f);
  c += texture2D(tex0, uv + vec2(-1.414, -1.414) * f);

  c += texture2D(tex0, uv + vec2(-3.0, 0.0) * f);
  c += texture2D(tex0, uv + vec2(-2.121, 2.121) * f);
  c += texture2D(tex0, uv + vec2(0.0, 3.0) * f);
  c += texture2D(tex0, uv + vec2(2.121, 2.121) * f);
  c += texture2D(tex0, uv + vec2(3.0, 0.0) * f);
  c += texture2D(tex0, uv + vec2(2.121, -2.121) * f);
  c += texture2D(tex0, uv + vec2(0.0, -3.0) * f);
  c += texture2D(tex0, uv + vec2(-2.121, -2.121) * f);
  
  c += texture2D(tex0, uv + vec2(-6.0, 0.0) * f);
  c += texture2D(tex0, uv + vec2(-4.243, 4.243) * f);
  c += texture2D(tex0, uv + vec2(0.0, 6.0) * f);
  c += texture2D(tex0, uv + vec2(4.243, 4.243) * f);
  c += texture2D(tex0, uv + vec2(6.0, 0.0) * f);
  c += texture2D(tex0, uv + vec2(4.243, -4.243) * f);
  c += texture2D(tex0, uv + vec2(0.0, -6.0) * f);
  c += texture2D(tex0, uv + vec2(-4.243, -4.243) * f);

  gl_FragColor = c * factor;
  gl_FragColor.a = unif[5][2];
}
