/////RADIAL BLUR FILTER/////
//www.cloneproduction.net
#include std_head_fs.inc

varying vec2 uv;

#define step 0.0625

void main(void){
  vec2 BlurXY = vec2 (unif[16]); //blur center position
  float Amount = unif[17][0]; //blur radial amount
  float BlurR = unif[17][1]; //blur rotation amount
  gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
  vec2 piv = vec2(BlurXY.x + 0.5, BlurXY.y + 0.5);
  float wd = texture2D(tex1, uv).x;
  vec2 d = (uv - piv); // from centre to this pixel
  // use radial vec = -dy, dx
  d = d * Amount * (1.0 + wd) + vec2(-d.y, d.x) * BlurR * (1.0 + wd);
  for (float i=0.0; i<1.0; i+=step){
    //attempt to stop 'wrapping'
    //vec2 duv = uv + d * pow(2.0, i);
    gl_FragColor += texture2D(tex0, uv + d * pow(2.0, i)) * step;
  }
  gl_FragColor.a = unif[5][2];
}
