#!/usr/bin/env python3
"""Original teaching diagrams. Sphere radii follow ideal nearest-neighbour packing."""
from pathlib import Path
import math

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE.parent/'assets'
FONT = HERE/'fonts/Lato-Regular.ttf'
BOLD = HERE/'fonts/Lato-Bold.ttf'
INK, MUTED = '#15191F', '#5C6573'
RED, TEAL, BLUE = '#B3263E', '#1D7F79', '#3474B8'


def text(draw, xy, message, size=38, color=INK, bold=False):
    draw.text(xy,message,fill=color,font=ImageFont.truetype(str(BOLD if bold else FONT),size))


def sphere(image, cx, cy, radius, color):
    r = int(radius)
    yy, xx = np.mgrid[-r:r+1,-r:r+1] / max(r,1)
    mask = xx*xx+yy*yy <= 1
    zz = np.sqrt(np.maximum(0,1-xx*xx-yy*yy))
    light = np.clip(-.4*xx-.5*yy+.76*zz,0,1)
    rgb = np.array(tuple(int(color[i:i+2],16) for i in (1,3,5)))
    shade = np.clip(rgb[None,None,:]*(.48+.55*light[:,:,None])+20*light[:,:,None]**8,0,255)
    pixels = np.zeros((2*r+1,2*r+1,4),dtype=np.uint8)
    pixels[:,:,:3],pixels[:,:,3] = shade,mask*255
    image.alpha_composite(Image.fromarray(pixels), (int(cx)-r,int(cy)-r))


def atoms(name, points, colors=None, caption='Idealized space-filling model'):
    image = Image.new('RGBA',(1600,1000),'white')
    draw = ImageDraw.Draw(image)
    coords = np.array(points,dtype=float)
    rx,rz = math.radians(25),math.radians(32)
    transform = np.array([[math.cos(rz),-math.sin(rz),0],
                          [math.sin(rz)*math.sin(rx),math.cos(rz)*math.sin(rx),-math.cos(rx)],
                          [math.sin(rz)*math.cos(rx),math.cos(rz)*math.cos(rx),math.sin(rx)]])
    coords = coords@transform.T
    spread = coords[:,:2].max(0)-coords[:,:2].min(0)
    scale = min(1250/(spread[0]+2),740/(spread[1]+2))
    center = (coords[:,:2].max(0)+coords[:,:2].min(0))/2
    for n in np.argsort(coords[:,2]):
        x,y=(coords[n,:2]-center)*scale+[800,440]
        sphere(image,x,y,scale,colors[n] if colors else BLUE)
    text(draw,(70,890),caption,32,MUTED)
    image.convert('RGB').save(OUT/name)


def fcc(n):
    a = 2*math.sqrt(2)
    return [(a*(x+i),a*(y+j),a*(z+k)) for i in range(n) for j in range(n) for k in range(n)
            for x,y,z in [(0,0,0),(.5,.5,0),(.5,0,.5),(0,.5,.5)]]


def boxes(name, entries, caption='', columns=None):
    columns = columns or len(entries)
    rows = math.ceil(len(entries)/columns)
    image = Image.new('RGB',(1600,1000),'white')
    draw = ImageDraw.Draw(image)
    cell_w,cell_h = 1440/columns,780/rows
    for n,(label,detail) in enumerate(entries):
        x,y = 80+(n%columns)*cell_w,70+(n//columns)*cell_h
        draw.rounded_rectangle((x,y,x+cell_w-26,y+cell_h-36),radius=18,fill='#F4F5F7')
        draw.rectangle((x,y,x+cell_w-26,y+8),fill=[RED,TEAL,BLUE][n%3])
        label_font=ImageFont.truetype(str(BOLD),36)
        label_lines=['']
        for word in label.split():
            candidate=(label_lines[-1]+' '+word).strip()
            if label_lines[-1] and draw.textlength(candidate,font=label_font)>cell_w-70:
                label_lines.append(word)
            else:
                label_lines[-1]=candidate
        for line_n,line in enumerate(label_lines):
            text(draw,(x+24,y+38+line_n*42),line,36,bold=True)
        for line_n,line in enumerate(detail.split('\n')):
            text(draw,(x+24,y+72+len(label_lines)*42+line_n*48),line,29,MUTED)
    text(draw,(80,910),caption,30,MUTED)
    image.save(OUT/name)


def mechanics():
    for kind in ('bond-length','bond-angle','torsion'):
        if kind == 'bond-length':
            atoms(kind+'.png',[(0,0,0),(2,0,0)],[BLUE,TEAL],
                  caption='Preferred separation. Overlap or separation costs potential energy.')
        elif kind == 'bond-angle':
            atoms(kind+'.png',[(2,0,0),(0,0,0),(-1,math.sqrt(3),0)],[BLUE,TEAL,RED],
                  caption='The angle is defined by three atom centres. Adjacent spheres touch.')
        else:
            atoms(kind+'.png',[(0,0,0),(2,0,0),(3,math.sqrt(3),0),(4,math.sqrt(3),math.sqrt(3))],
                  [BLUE,TEAL,RED,BLUE],caption='Four atom centres define a twist around the middle connection.')


def landscape():
    image = Image.new('RGB',(1600,1000),'white')
    draw = ImageDraw.Draw(image)
    draw.line((160,780,1480,780),fill=MUTED,width=3)
    draw.line((160,780,160,140),fill=MUTED,width=3)
    xs = np.linspace(-1.45,1.45,500)
    ys = (xs*xs-1)**2+.08*xs
    points = [(160+(x+1.45)/2.9*1280,730-y*430) for x,y in zip(xs,ys)]
    draw.line(points,fill=BLUE,width=7)
    text(draw,(180,100),'Potential energy',36,bold=True)
    text(draw,(720,820),'A coordinate describing atomic arrangement',32,MUTED)
    text(draw,(240,575),'A nearby minimum',34,TEAL)
    text(draw,(860,330),'Energy barrier',34,RED)
    text(draw,(90,920),'Illustrative landscape. A minimization can stop in a local minimum.',30,MUTED)
    image.save(OUT/'minimization.png')


def main():
    OUT.mkdir(exist_ok=True)
    atoms('atoms.png',[(0,0,0)],caption='One sphere stands in for an atom and its electron cloud.')
    atoms('atoms-molecules.png',[(0,0,0),(2,0,0),(3,math.sqrt(3),0)],
          [BLUE,TEAL,RED],caption='A connected group of atoms. Sphere sizes here are schematic.')
    atoms('rh-crystal.png',fcc(2),caption='Ideal fcc Rh. Sphere radius = half the nearest-neighbour distance.')
    a=2*math.sqrt(2)
    cell=[(i*a,j*a,k*a) for i in (0,1) for j in (0,1) for k in (0,1)]
    cell += [(a*x,a*y,a*z) for x,y,z in [(0,.5,.5),(1,.5,.5),(.5,0,.5),(.5,1,.5),(.5,.5,0),(.5,.5,1)]]
    atoms('rh-cell.png',cell,caption='Conventional fcc cell. Shared corners and faces contribute four atoms per cell.')
    atoms('rh-supercell.png',fcc(5),caption='5 × 5 × 5 conventional fcc cells contain 500 atoms. Idealized geometry.')
    layer = [(2*i+(j%2),math.sqrt(3)*j,0) for i in range(7) for j in range(6)]
    slab = layer+[(x+1,y+math.sqrt(3)/3,math.sqrt(8/3)) for x,y,z in layer]
    atoms('rh-surface.png',slab,caption='Idealized close-packed surface. A slab exposes two faces.')
    atoms('bonded.png',[(0,0,0),(2,0,0),(3,math.sqrt(3),0),(5,math.sqrt(3),0)],
          [BLUE,TEAL,RED,BLUE],caption='Connected atoms can stretch, bend and twist. No bonds are drawn as sticks.')
    atoms('nonbonded.png',[(0,0,0),(3,0,0)],[RED,BLUE],
          caption='Space-filling atom models can interact across a gap without a chemical bond.')
    mechanics()
    landscape()
    boxes('md-loop.png',[('Forces','Differentiate the\npotential energy.'),
          ('Move atoms','Update velocities\nand positions.'),
          ('Repeat','Use a short time step\nand sample observables.')],
          'Molecular dynamics integrates an equation of motion. This is a workflow diagram.')
    boxes('simulation.png',[('Choose a question','Define a material\nand an observable.'),
          ('Run a model','Compute interactions\nunder stated conditions.'),
          ('Check evidence','Compare predictions\nwith measurements.')],
          'A model experiment answers a specific question under specific assumptions.')
    boxes('cost-ladder.png',[('Quantum / DFT','Describe electrons.\nSmall systems or\nshort time spans.'),
          ('Classical / IFF','Use fitted interactions.\nMore atoms and\nlonger sampling.'),
          ('Learned potential','Learn reference energies.\nCheck training coverage\nand sampling.')],
          'Cost and accuracy depend on the system, software, hardware and reference.')
    boxes('workflow.png',[(str(n+1)+'. '+name,detail) for n,(name,detail) in enumerate([
          ('Intake','State the question.'),('References','Trace primary data.'),
          ('Model','Declare the physics.'),('Contract','Fix the tests and units.'),
          ('Run and fit','Keep inputs and results.'),('Validate','Test independent evidence.'),
          ('Export readback','Check exported meaning.'),('Review and disposition','Accept, restrict or reject.')])],
          'Workflow repeatability does not by itself establish scientific accuracy.',columns=4)


if __name__=='__main__':
    main()
