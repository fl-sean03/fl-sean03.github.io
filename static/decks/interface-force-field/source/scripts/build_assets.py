#!/usr/bin/env python3
"""Deterministic original visuals. No materials simulation is run by this script."""
from pathlib import Path
import json,csv,math,subprocess,os,sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
from PIL import Image,ImageDraw,ImageFont
from ase import Atoms
from ase.build import bulk,fcc111
from ase.io import write
ROOT=Path(__file__).resolve().parents[1];os.chdir(ROOT)
BG='#FBFAF7';FG='#1B1B1A';MUT='#5C5A55';TEAL='#166D66';GOLD='#80530C';BLUE='#315FA2';RED='#A23447'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'text.color':FG,'axes.labelcolor':FG,'xtick.color':MUT,'ytick.color':MUT,'axes.edgecolor':MUT,'axes.facecolor':BG,'figure.facecolor':BG,'savefig.facecolor':BG,'axes.spines.top':False,'axes.spines.right':False})
Path('media').mkdir(exist_ok=True);Path('data').mkdir(exist_ok=True)
# Rh cell: corrected source CAR contains the symmetry-unique site in Fm-3m.
a=3.8032
rh=bulk('Rh','fcc',a=a,cubic=True)
supercell=rh.repeat((3,3,3));slab=fcc111('Rh',size=(6,4,6),a=a,vacuum=7,orthogonal=True)
write('data/rh-unit.cif',rh);write('data/rh-supercell.xyz',supercell);write('data/rh111-slab.extxyz',slab)
Path('data/geometry.json').write_text(json.dumps({'element':'Rh','phase':'fcc','space_group':'Fm-3m (225)','a_angstrom':a,'unit_atoms':len(rh),'supercell_atoms':len(supercell),'slab_atoms':len(slab),'slab_orientation':'(111)','slab_inplane_vectors_angstrom':slab.cell.array.tolist(),'reconstruction':'Fm-3m symmetry expansion from corrected rh_unit_cell_Fm3m.car; slab via ASE fcc111; static ideal source-grounded construction, not relaxed simulation','source':'Kanhaiya 2021 corrected Supplementary Data; author correction DOI 10.1038/s41524-021-00576-8'},indent=2))

def frame_3d(atoms,path,az=35,elev=21,unit=False,labels=True):
 fig=plt.figure(figsize=(10,7),dpi=140);ax=fig.add_subplot(111,projection='3d');p=atoms.positions
 if unit:
  # Include equivalent boundary sites for legible conventional-cell drawing.
  q=[]
  for i in range(3):
   for j in range(3):
    for k in range(3):
     v=np.array([i,j,k])/2
     if (i+j+k)%2==0:q.append(v*a)
  p=np.array(q)
 z=p[:,2]
 # Opaque light-dependent sphere tones preserve contrast against the pale ground.
 colors=[]
 for zz in z:
  base=TEAL if zz>z.max()-.1 else BLUE
  shade=.76+.24*(zz-z.min())/max(float(np.ptp(z)),1)
  colors.append(tuple(int(base[i:i+2],16)/255*shade for i in (1,3,5)))
 ax.scatter(p[:,0],p[:,1],p[:,2],s=460 if unit else 145,c=colors,edgecolors=FG,linewidths=.8,alpha=1,depthshade=False)
 if unit:
  for dim in range(3):
   for b in [0,a]:
    for c in [0,a]:
     s=np.zeros(3);e=np.zeros(3);s[dim]=0;e[dim]=a;other=[i for i in range(3) if i!=dim];s[other]=[b,c];e[other]=[b,c];ax.plot(*zip(s,e),color=MUT,alpha=1,lw=1)
 ax.set_box_aspect(np.maximum(np.ptp(p,axis=0),1));ax.view_init(elev=elev,azim=az);ax.set_axis_off();ax.set_proj_type('ortho')
 fig.subplots_adjust(0,0,1,1);fig.savefig(path);plt.close(fig)
frame_3d(rh,'media/rh-unit.png',unit=True)
frame_3d(supercell,'media/rh-supercell.png')
frame_3d(slab,'media/rh111-slab.png',az=34,elev=23)
# Original coordination drawing: nearest neighbor layer on Rh(111), source-derived distance.
fig,ax=plt.subplots(figsize=(9,6));d=a/math.sqrt(2)
pts=np.array([[math.cos(t),math.sin(t)] for t in np.arange(6)*math.pi/3])*d
for p in pts:ax.plot([0,p[0]],[0,p[1]],color=MUT,alpha=1,lw=2)
ax.scatter(pts[:,0],pts[:,1],s=850,color=BLUE,edgecolor=FG,lw=1);ax.scatter([0],[0],s=1000,color=TEAL,edgecolor=FG)
ax.annotate('in-plane nearest neighbor\n2.6893 Å',xy=pts[0]/2,xytext=(.1,-3.3),color=FG,arrowprops={'arrowstyle':'->','color':GOLD},fontsize=16)
ax.set_aspect('equal');ax.set_xlim(-4,4);ax.set_ylim(-4,3.7);ax.axis('off');fig.savefig('media/rh111-neighbors.png',dpi=180,bbox_inches='tight');plt.close(fig)
# Physically defined illustrative potentials in reduced units, authors' Rmin convention.
x=np.linspace(.83,2.6,600);u=x**-12-2*x**-6;f=12*(x**-13-x**-7)
np.savetxt('data/lj-reduced.csv',np.c_[x,u,f],delimiter=',',header='r_over_Rmin,U_over_epsilon,F_times_Rmin_over_epsilon',comments='')
fig,axs=plt.subplots(2,1,figsize=(9,6),sharex=True,gridspec_kw={'height_ratios':[1,1]})
axs[0].plot(x,u,color=TEAL,lw=3);axs[0].axhline(0,color=MUT,lw=.7);axs[0].scatter([1],[-1],s=70,color=GOLD,zorder=4);axs[0].text(1.14,-.8,'minimum: r = Rmin',fontsize=14);axs[0].set_ylabel('U / ε');axs[0].set_ylim(-1.4,2.8)
axs[1].plot(x,f,color=GOLD,lw=3);axs[1].axhline(0,color=MUT,lw=.7);axs[1].set_ylabel('Fr Rmin / ε');axs[1].set_xlabel('Separation r / Rmin');axs[1].set_ylim(-5,12)
for ax in axs:ax.grid(alpha=.12);ax.set_xlim(.83,2.6)
fig.tight_layout();fig.savefig('media/energy-force.png',dpi=180);plt.close(fig)
# Numerical published data, exact transcription of main Tables 2, 3 and 5.
rows=[['Ca (α)',27.942,27.947,27.953,.492,.01,.490,.490,20,30,21],['Rh',19.016,19.016,19.014,2.64,.02,2.643,2.643,276,258,175],['Sr (α)',30.420,30.423,30.421,.41,.01,.411,.410,12,24,16]]
header=['metal','five_a_expt_A','five_a_LJ12_6_A','five_a_LJ9_6_A','gamma111_expt_J_m2','gamma111_expt_unc_J_m2','gamma111_LJ12_6_J_m2','gamma111_LJ9_6_J_m2','K_expt_selected_GPa','K_LJ12_6_GPa','K_LJ9_6_GPa']
with open('data/published-results.csv','w') as fh:w=csv.writer(fh);w.writerow(header);w.writerows(rows)
with open('data/rh-parameters.csv','w') as fh:w=csv.writer(fh);w.writerow(['family','Rmin_A','epsilon_kcal_mol','source']);w.writerows([['12-6',2.757,7.84,'Kanhaiya2021 Table1'],['9-6',2.807,6.38,'Kanhaiya2021 Table1']])

def results_chart(which,path):
 fig,ax=plt.subplots(figsize=(10,6),dpi=160)
 if which=='calibration':
  names=['Ca (α)','Rh','Sr (α)'];pos=np.arange(3);ex=np.array([r[4] for r in rows]);unc=[r[5] for r in rows]
  ax.errorbar(pos-.12,ex,yerr=unc,fmt='o',color=FG,ms=9,capsize=5,label='Experimental reference')
  ax.scatter(pos+.02,[r[6] for r in rows],s=85,c=TEAL,label='12–6 LJ');ax.scatter(pos+.14,[r[7] for r in rows],s=70,c=GOLD,marker='D',label='9–6 LJ')
  ax.set_xticks(pos,names);ax.set_ylabel('(111) surface energy / J m⁻²');ax.set_ylim(0,3.1)
  for i,r in enumerate(rows):ax.text(i,r[4]+.14,f'{r[4]:g} ± {r[5]:g}',ha='center',fontsize=12)
  ax.legend(loc='upper left',frameon=False,labelcolor=FG,fontsize=12);ax.grid(axis='y',alpha=.12)
 elif which=='bulk':
  pos=np.arange(3);w=.22
  for k,c,l,off in [(8,FG,'Experiment (selected reference)',-w),(9,TEAL,'12–6 LJ',0),(10,GOLD,'9–6 LJ',w)]:
   vals=[r[k] for r in rows];bars=ax.bar(pos+off,vals,w,color=c,label=l)
   ax.bar_label(bars,fontsize=12,padding=4,color=c)
  ax.set_xticks(pos,[r[0] for r in rows]);ax.set_ylabel('Bulk modulus K / GPa');ax.set_ylim(0,335);ax.legend(frameon=False,labelcolor=FG,fontsize=12);ax.grid(axis='y',alpha=.1)
 elif which=='rh':
  vals=[276,258,175];pos=np.arange(3);colors=[FG,TEAL,GOLD]
  bars=ax.barh(pos,vals,color=colors,height=.55);ax.set_yticks(pos,['Experiment','12–6 LJ','9–6 LJ']);ax.invert_yaxis();ax.set_xlabel('Bulk modulus K / GPa');ax.set_xlim(0,335)
  for i,v in enumerate(vals):ax.text(v+6,i,str(v),va='center',fontsize=18,color=colors[i])
  ax.text(320,.8,'−6.5%',ha='right',color=TEAL,fontsize=17);ax.text(320,1.8,'−36.6%',ha='right',color=GOLD,fontsize=17);ax.grid(axis='x',alpha=.12)
 fig.tight_layout();fig.savefig(path);plt.close(fig)
results_chart('calibration','media/calibration.png');results_chart('bulk','media/bulk-validation.png');results_chart('rh','media/rh-validation.png')
# Illustrative charge redistribution values (SI Table S2); do not reproduce original figures.
fig,ax=plt.subplots(figsize=(9,5));vals=[5.49,4.57,2.59];bars=ax.barh(range(3),vals,color=[TEAL,BLUE,GOLD],height=.6);ax.set_yticks(range(3),['First shell: 100/0','First + second: 67/33','Second shell: 0/100']);ax.invert_yaxis();ax.set_xlim(0,6.5);ax.set_xlabel('Raw Ni-vacancy defect energy / eV')
for i,v in enumerate(vals):ax.text(v+.12,i,f'{v:.2f}',va='center',fontsize=18)
ax.grid(axis='x',alpha=.1);fig.tight_layout();fig.savefig('media/alloy-defect.png',dpi=170);plt.close(fig)
# Motion sequences: render 720p frames with permanently visible provenance and subtitles.
FONT='DejaVuSans.ttf'
font=ImageFont.truetype(FONT,28);small=ImageFont.truetype(FONT,19);big=ImageFont.truetype(FONT,40)
W,H=1280,720;FPS=12

def canvas(title,sub,label):
 im=Image.new('RGB',(W,H),BG);dr=ImageDraw.Draw(im);dr.text((52,30),title,font=big,fill=FG);dr.text((52,89),sub,font=font,fill=MUT);dr.rectangle((52,665,1228,666),fill=MUT);dr.text((52,680),label,font=small,fill=GOLD);return im,dr

def save_frames(name,frames):
 folder=Path('media/frames/'+name);folder.mkdir(parents=True,exist_ok=True)
 for i,im in enumerate(frames):im.save(folder/f'{i:04d}.png')
 cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-threads','4','-framerate',str(FPS),'-i',str(folder/'%04d.png'),'-c:v','libx264','-threads','4','-pix_fmt','yuv420p','-crf','20','-movflags','+faststart',f'media/{name}.mp4'];subprocess.run(cmd,check=True)
 # Deterministic 6fps animated fallback. Poster is a motion peak rather than black opening.
 frames[::2][0].save(f'media/{name}.gif',save_all=True,append_images=frames[::2][1:],duration=[170 if j%3!=2 else 160 for j in range(len(frames[::2]))],loop=0,optimize=True)
 frames[len(frames)*5//6 if name=='structure-walkthrough' else len(frames)//2].save(f'media/{name}-poster.png')

if not sys.argv[1:] or 'structure' in sys.argv[1:]:
 # Sequence 1: authentic geometry, camera and stage transitions only.
 frames=[]
 for i in range(9*FPS):
  t=i/FPS;stage=min(int(t//3),2);atoms=[rh,supercell,slab][stage];title=['One periodic unit cell','Replicate the lattice','Expose a (111) surface'][stage]
  temp=Path('media/frames/_structure.png');temp.parent.mkdir(parents=True,exist_ok=True);frame_3d(atoms,temp,az=25+30*(t%3)/3,unit=stage==0)
  im,dr=canvas('Rhodium · from cell to surface',title+'  |  a = 3.8032 Å','Static ideal geometry from corrected Kanhaiya 2021 data; camera motion only')
  tile=Image.open(temp).convert('RGB').resize((770,539));im.paste(tile,(260,120));dr=ImageDraw.Draw(im)
  dr.text((52,200),['Fm-3m','3 × 3 × 3','(111) slab'][stage],font=font,fill=TEAL);dr.text((52,245),['4 atoms/cell','108 atoms','144 atoms'][stage],font=small,fill=FG)
  dr.text((52,300),'Rh · bulk',font=small,fill=BLUE);dr.text((52,334),'Rh · top layer',font=small,fill=TEAL)
  # native projected structure has valid dimensions; explicit length scale.
  dr.text((1010,585),'a = 3.8032 Å',font=small,fill=FG)
  dr.text((1010,626),'cubic cell parameter',font=small,fill=MUT) # not a projected metric bar
  frames.append(im)
 save_frames('structure-walkthrough',frames)
if not sys.argv[1:] or 'model' in sys.argv[1:]:
 # Sequence 2: analytical two-atom pedagogical motion, no materials MD claim.
 frames=[]
 for i in range(10*FPS):
  t=i/FPS;r=1+.23*math.cos(2*math.pi*t/3)*math.exp(-t/5);u=r**-12-2*r**-6;fr=12*(r**-13-r**-7)
  im,dr=canvas('Energy → force → operation','U = ε [(Rmin/r)¹² − 2(Rmin/r)⁶]','Illustrative prescribed two-atom motion; not an IFF materials trajectory')
  left=350;right=350+260*r
  dr.ellipse((left-44,288-44,left+44,288+44),fill=BLUE);dr.ellipse((right-44,288-44,right+44,288+44),fill=TEAL)
  dr.line((left,353,right,353),fill=FG,width=2);dr.text((430,370),f'r / Rmin = {r:.3f}',font=font,fill=FG)
  # force on atom at +r: Fr positive outward, negative inward.
  end=right+int(np.clip(fr*13,-100,100))
  if abs(end-right)>=1:
   dr.line((right,450,end,450),fill=GOLD,width=5);sg=1 if end>=right else -1;dr.polygon([(end,450),(end-12*sg,442),(end-12*sg,458)],fill=GOLD)
  dr.text((780,260),f'U / ε = {u:.3f}',font=font,fill=TEAL);dr.text((780,315),f'Fr Rmin / ε = {fr:.3f}',font=font,fill=GOLD)
  dr.text((52,530),'Minimize: seek a lower-energy configuration',font=font,fill=FG);dr.text((52,577),'MD: integrate forces with mass, time step and ensemble',font=font,fill=FG)
  frames.append(im)
 save_frames('model-walkthrough',frames)
if not sys.argv[1:] or 'evidence' in sys.argv[1:]:
 # Sequence 3: reveal actual published comparisons; 12-6 and 9-6 are alternatives, not temporal revisions.
 frames=[]
 for i in range(12*FPS):
  t=i/FPS;stage=min(int(t//4),2);im,dr=canvas('Calibration → independent prediction',['Fit: lattice and (111) surface energy','Test: bulk modulus was not fitted','Decide: qualify the intended observable'][stage],'Published Kanhaiya 2021 Tables 2, 3, 5; animation reveals data, not new simulation')
  if stage==0:
   dr.text((100,205),'Rh · 298 K',font=big,fill=TEAL);dr.text((100,275),'5a  19.016 Å → 19.016 Å (12–6)',font=font,fill=FG);dr.text((100,345),'γ111  2.64 ± 0.02 → 2.643 J/m²',font=font,fill=FG);dr.text((100,445),'These are calibration agreements.',font=big,fill=GOLD)
  elif stage==1:
   tile=Image.open('media/rh-validation.png').convert('RGB').resize((830,498));im.paste(tile,(230,144));dr=ImageDraw.Draw(im);dr.text((52,176),'Rh · K',font=font,fill=TEAL)
  else:
   dr.text((100,205),'Surface fit does not guarantee elasticity.',font=big,fill=FG);dr.text((100,292),'12–6: K = 258 GPa  (−6.5%)',font=font,fill=TEAL);dr.text((100,350),'9–6: K = 175 GPa  (−36.6%)',font=font,fill=GOLD);dr.text((100,440),'Change model family? Start a new contract',font=font,fill=FG);dr.text((100,490),'and reserve fresh validation evidence.',font=font,fill=FG);dr.text((100,565),'12–6 / 9–6 are published alternatives, not a fitted revision.',font=small,fill=MUT)
  frames.append(im)
 save_frames('evidence-walkthrough',frames)
print('Built geometry, five charts, and 3 MP4/GIF/poster sequences.')
